import os
import boto3
from htmlResponse import htmlResponse
from htmlForbiddenResponse import htmlForbiddenResponse

DEFAULT_REGION = 'us-west-2'
DEFAULT_CLUSTER = 'minecraft'
DEFAULT_SERVICE = 'minecraft-server'

REGION = os.environ.get('REGION', DEFAULT_REGION)
CLUSTER = os.environ.get('CLUSTER', DEFAULT_CLUSTER)
SERVICE = os.environ.get('SERVICE', DEFAULT_SERVICE)
WHITELIST = os.environ.get('WHITELIST', ["ebf490c7-31c3-4554-8c38-71b5b69f9aa1", "778aeda1-1100-4497-841c-357a3ba27f10"])

if REGION is None or CLUSTER is None or SERVICE is None:
    raise ValueError("Missing environment variables")

def lambda_handler(event, context):
    """Updates the desired count for a service."""
    userUUID = event["requestContext"]["http"]["path"][1:]
    if userUUID not in WHITELIST:
        return {
      "statusCode": 200,
      "headers": {
        'Content-Type': 'text/html',
      },
      "body": htmlForbiddenResponse()
    }
    
    ecs = boto3.client('ecs', region_name=REGION)
    response = ecs.describe_services(
        cluster=CLUSTER,
        services=[SERVICE],
    )

    desired = response["services"][0]["desiredCount"]

    if desired == 0:
        ecs.update_service(
            cluster=CLUSTER,
            service=SERVICE,
            desiredCount=1,
        )
        print("Updated desiredCount to 1")
    else:
        print("desiredCount already at 1")
    
    result = {
      "statusCode": 200,
      "headers": {
        'Content-Type': 'text/html',
      },
      "body": htmlResponse()
    }
    
    return result