import json
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
import boto3

client = boto3.client('glue')
glue = boto3.client(service_name='glue', region_name='us-west-2',
                    endpoint_url='https://glue.us-west-2.amazonaws.com')
# step-fn-activity
client_sf = boto3.client('stepfunctions')
# replace activity arn with respective activivty arn
activity = "arn:aws:states:us-west-2:XXXXXXXXXXXX:activity:file-transfer"


def lambda_handler(event, context):
    # TODO implement
    print("Starting Glue Crawler")

    class CrawlerException(Exception):
        pass

    try:
        response = client.start_crawler(Name='raw-refined-crawler')
    except CrawlerRunningException as c:
        raise CrawlerException('Crawler In Progress!')
        print('Crawler in progress')
    except Exception as e:
        # send activity failure token
        task = client_sf.get_activity_task(activityArn=activity, workerName='raw-refined-crawler')
        response = client_sf.send_task_failure(taskToken=task['taskToken'])
        print('Problem while invoking crawler')