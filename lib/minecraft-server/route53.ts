import { RemovalPolicy, Duration } from 'aws-cdk-lib';
import { PolicyStatement, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { ILogGroup, LogGroup, ResourcePolicy, RetentionDays } from 'aws-cdk-lib/aws-logs';
import { HostedZone, ARecord, NsRecord, IHostedZone,  } from 'aws-cdk-lib/aws-route53';
import { CfnResolverQueryLoggingConfig } from 'aws-cdk-lib/aws-route53resolver';
import { Construct } from 'constructs';

interface Route53ResourcesProps {
  serverSubDomain: string;
  domain: string;
  hostedZoneId: string;
}

export class Route53Resources extends Construct {
  queryLogGroup: ILogGroup;
  hostedZone: IHostedZone;
  subDomainZoneId: string;

  constructor(scope: Construct, id: string, props: Route53ResourcesProps) {
    super(scope, id);

    // new ResourcePolicy(this, 'ResourcePolicy', {
    //   policyStatements: [
    //     new PolicyStatement({
    //       principals: [new ServicePrincipal('route53.amazonaws.com')],
    //       actions: ['logs:CreateLogStream', 'logs:PutLogEvents'],
    //       resources: [props.queryLogsLogGroupArn],
    //     }),
    //   ],
    // });
    
    this.hostedZone = HostedZone.fromHostedZoneAttributes(this, 'HostedZone', {
      hostedZoneId: props.hostedZoneId,
      zoneName: 'cloudsnake.nl'
    });
    // const subdomainHostedZone = new HostedZone(this, 'SubdomainHostedZone', {
    //   zoneName: props.serverSubDomain + '.' + props.domain,
    //   // queryLogsLogGroupArn: props.queryLogsLogGroupArn,
    // });

    // new NsRecord(this, 'SubdomainNsRecord', {
    //   zone: hostedZone,
    //   values: subdomainHostedZone.hostedZoneNameServers as string[],
    //   recordName: props.serverSubDomain + '.' + props.domain,
    // });

    new ARecord(this, 'clientSiteARecord', {
      zone: this.hostedZone,
      target: { values: ['192.168.1.1'] },
      ttl: Duration.seconds(30),
      recordName: props.serverSubDomain + '.' + props.domain,
    });
    this.subDomainZoneId = this.hostedZone.hostedZoneId;
  }
}