import json
import boto3

sqs = boto3.client('sqs', region_name='us-east-1')


def lambda_handler(event, context):
    # queue_url='https://sqs.us-east-1.amazonaws.com/116263928116/LambdaDemo'

    print("Test Lambda SQS")
    print('event')

    doc = event['Records'][0]

    print(doc)
    print('**********')
    print(doc['body'])