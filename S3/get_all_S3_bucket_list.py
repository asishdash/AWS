import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': lists3()
    }

def lists3():
    bucket_list = []
    for bucket in s3.buckets.all():
	    print(bucket.name)
	    bucket_list.append(bucket.name)
    return bucket_list