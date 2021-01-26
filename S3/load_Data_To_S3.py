import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='YOUR BUCKET NAME'

	transactionToUpload = {}
	transactionToUpload['transactionId'] = '1'
	transactionToUpload['type'] = 'sell'
	transactionToUpload['amount'] = 200
	transactionToUpload['customerId'] = 'X01'

	fileName = 'data_load' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Complete')