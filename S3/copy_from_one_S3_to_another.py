import json
import boto3

s3_resource = boto3.resource('s3')
s3 =  boto3.client('s3')

def lambda_handler(event, context):
    listncopy()


def listncopy():
    bucket = 'tbuck1aj'
    newbucket = 'tbuck1aj2'
    try:
        response = s3.list_objects(
            Bucket=bucket,
            MaxKeys=5
        )

        for record in response['Contents']:
            key = record['Key']
            copy_source = {
                'Bucket': bucket,
                'Key': key
            }
            try:
                print(copy_source)
                destbucket = s3_resource.Bucket(newbucket)
                destbucket.copy(copy_source,key)

            except Exception as e:
                print(e)
                print('Error getting object {} from bucket {}. '.format(key, bucket))
                raise e
    except Exception as e:
        print(e)
        raise e
