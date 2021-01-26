import boto3

s3 =  boto3.client('s3')
bucket = 'tbuck1aj'

def lambda_handler(event, context):
    listndwnld()

def listndwnld():
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
                s3.download_file(copy_source['Bucket'], copy_source['Key'], copy_source['Key'])

            except Exception as e:
                print(e)
                print('Error getting object {} from bucket {}. '.format(key, bucket))
                raise e
    except Exception as e:
        print(e)
        raise e

