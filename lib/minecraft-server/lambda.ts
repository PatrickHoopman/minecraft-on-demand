import { Stack } from 'aws-cdk-lib';
import { Cluster, FargateService } from 'aws-cdk-lib/aws-ecs';
import {
  Role,
  ServicePrincipal,
  ManagedPolicy,
  PolicyDocument,
  PolicyStatement,
} from 'aws-cdk-lib/aws-iam';
import { Function, FunctionUrl, Code, Runtime, Architecture, FunctionUrlAuthType } from 'aws-cdk-lib/aws-lambda';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

interface LambdaResourcesProps {
  cluster: Cluster;
  service: FargateService;
  serverSubDomain: string;
  domain: string;
}

export class LambdaResources extends Construct {
  launcherFunctionUrl: string;
  constructor(scope: Construct, id: string, props: LambdaResourcesProps) {
    super(scope, id);

    const lambdaRole = new Role(this, 'LambdaRole', {
      assumedBy: new ServicePrincipal('lambda.amazonaws.com'),
      inlinePolicies: {
        ['ecsPolicy']: new PolicyDocument({
          statements: [
            new PolicyStatement({
              resources: [
                `${props.service.serviceArn}/*`,
                props.service.serviceArn,
                `${props.cluster.clusterArn}/*`,
                props.cluster.clusterArn,
              ],
              actions: ['ecs:*'],
            }),
          ],
        }),
      },
      managedPolicies: [
        ManagedPolicy.fromAwsManagedPolicyName(
          'service-role/AWSLambdaBasicExecutionRole',
        ),
      ],
    });

    const launchFunction = new Function(this, 'LauncherLambda', {
      code: Code.fromAsset('lib/minecraft-server/resources/lambda'),
      role: lambdaRole,
      handler: 'index.lambda_handler',
      runtime: Runtime.PYTHON_3_9,
      logRetention: RetentionDays.ONE_WEEK,
      architecture: Architecture.ARM_64,
      environment: {
        REGION: Stack.of(this).region,
        CLUSTER: props.cluster.clusterName,
        SERVICE: props.service.serviceName,
      }
    });
    const functionUrl = new FunctionUrl(this, 'LaunchFunctionUrl', {
      function: launchFunction,
      authType: FunctionUrlAuthType.NONE
    })
    this.launcherFunctionUrl = functionUrl.url
  }
}