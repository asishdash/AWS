import boto3

s3obj = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('empl')


def lambda_handler(event, context):
    #	--bucket_name = event['Records'][0]['s3']['bucket']['name']
    #	--file_name = event['Records'][0]['s3']['object']['key']
    bucket_name = 'dynamotos3data'
    file_name = 'samplefile/emp.csv'

    resp = s3obj.get_object(Bucket=bucket_name, Key=file_name)

    data = resp['Body'].read().decode('utf-8')
    employees = data.split('\n')
    print(employees)

    for emp in employees:
        emp_id, emp_name, emp_prof = emp.split(',')

        try:
            response = table.put_item(
                Item={
                    "emp_id": emp_id,
                    "emp_name": emp_name,
                    "emp_prof": emp_prof
                }
            )
        except Exception as e:
            raise e