/* eslint-disable import/no-extraneous-dependencies */
import { App, Duration, Fn, Stack, StackProps } from "aws-cdk-lib";
import { Port } from "aws-cdk-lib/aws-ec2";
import { Protocol } from "aws-cdk-lib/aws-ecs";
import { Topic } from "aws-cdk-lib/aws-sns";
import { Construct } from "constructs";
import { config } from "dotenv";
import {
  VPCResources,
  ECSResources,
  SNSResources,
  Route53Resources,
  LambdaResources,
} from "../lib/minecraft-server";
import { ARecord, RecordTarget } from "aws-cdk-lib/aws-route53";
import { CloudFrontWebDistribution, Distribution, PriceClass } from "aws-cdk-lib/aws-cloudfront";
import { CloudFrontTarget } from "aws-cdk-lib/aws-route53-targets";
import { HttpOrigin } from "aws-cdk-lib/aws-cloudfront-origins";
import { Certificate } from "aws-cdk-lib/aws-certificatemanager";

config();

interface MinecraftProps extends StackProps {
  minecraftEdition: string;
  serverSubDomain: string;
  domain: string;
  hostedZoneId: string;
  memorySize: string;
  cpuSize: string;
  snsEmail?: string;
  startupMin: string;
  shutdownMin: string;
  debug: string;
}

export interface ServerConfig {
  port: number;
  protocol: Protocol;
  image: string;
  debug: boolean;
  ingressRule: Port;
}

export class Minecraft extends Stack {
  constructor(scope: Construct, id: string, props: MinecraftProps) {
    super(scope, id, props);

    let serverConfig: ServerConfig;

    if (props.minecraftEdition === "java") {
      serverConfig = {
        port: 25565,
        protocol: Protocol.TCP,
        image: "itzg/minecraft-server",
        debug: props.debug === "true" ? true : false,
        ingressRule: Port.tcp(25565),
      };
    } else {
      serverConfig = {
        port: 19132,
        protocol: Protocol.UDP,
        image: "itzg/minecraft-bedrock-server",
        debug: props.debug === "true" ? true : false,
        ingressRule: Port.udp(19132),
      };
    }

    const vpcResources = new VPCResources(this, "VPCResources", {
      ingressRule: serverConfig.ingressRule,
    });

    let snsTopic: Topic;

    if (props.snsEmail) {
      const snsResources = new SNSResources(this, "SNSResources", {
        snsEmail: props.snsEmail,
      });
      snsTopic = snsResources.snsTopic;
    }

    const route53 = new Route53Resources(this, "Route53Resources", {
      hostedZoneId: props.hostedZoneId,
      serverSubDomain: props.serverSubDomain,
      domain: props.domain,
    });

    const ecsResources = new ECSResources(this, "ECSResources", {
      snsTopic: snsTopic!,
      memorySize: props.memorySize,
      cpuSize: props.cpuSize,
      vpc: vpcResources.vpc,
      securityGroup: vpcResources.securityGroup,
      serverSubDomain: props.serverSubDomain,
      domain: props.domain,
      hostedZoneId: props.hostedZoneId,
      subDomainHostedZoneId: route53.subDomainZoneId,
      minecraftEdition: props.minecraftEdition,
      startupMin: props.startupMin,
      shutdownMin: props.shutdownMin,
      serverConfig: serverConfig,
    });

    const { launcherFunctionUrl } = new LambdaResources(
      this,
      "LambdaResources",
      {
        cluster: ecsResources.cluster,
        service: ecsResources.service,
        serverSubDomain: props.serverSubDomain,
        domain: props.domain,
      }
    );

    const cfDistribution = new Distribution(this, "CFDistribution", {
      priceClass: PriceClass.PRICE_CLASS_100,
      domainNames: [`launch-${props.serverSubDomain}.${props.domain}`],
      certificate:  Certificate.fromCertificateArn(this, 'CloudsnakeCertificate', 'arn:aws:acm:us-east-1:476098654112:certificate/98abe87f-3c15-4c89-a3fe-800a1efe3aae'),
      defaultBehavior: {
        origin: new HttpOrigin(Fn.select(2, Fn.split('/', launcherFunctionUrl)))
      }
    });

    new ARecord(this, 'LauncherSubdomain', {
      zone: route53.hostedZone,
      target: RecordTarget.fromAlias(new CloudFrontTarget(cfDistribution)),
      ttl: Duration.seconds(30),
      recordName: `launch-${props.serverSubDomain}.${props.domain}`,
    })
  }
}

// for development, use account/region from cdk cli
const devEnv = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const app = new App();

const stackProps = {
  minecraftEdition: process.env.MINECRAFT_EDITION || "java",
  serverSubDomain: process.env.SERVER_SUBDOMAIN || "minecraft",
  domain: process.env.DOMAIN || "example.com",
  hostedZoneId: process.env.HOSTED_ZONE_ID || "Z00000000000000000000",
  memorySize: process.env.MEMORY_SIZE || "8192",
  cpuSize: process.env.CPU_SIZE || "4096",
  snsEmail: process.env.SNS_EMAIL || "",
  startupMin: process.env.STARTUP_MIN || "10",
  shutdownMin: process.env.SHUTDOWN_MIN || "20",
  debug: process.env.DEBUG || "false",
};

new Minecraft(app, "Minecraft", {
  ...stackProps,
  env: devEnv,
});

app.synth();
