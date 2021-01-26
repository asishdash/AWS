import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
   bucket = 'YOUR BUCKET NAME'
   key = 'transactions.json'

   response = s3.get_object(Bucket=bucket, Key=key)

   content = response['Body']

   jsonObject = json.loads(content.read())

   transactions = jsonObject['transactions']

   for record in transactions:
      print("TransactionType: " + record['transType'])
      print("TransactionAmount: " + str(record['amount']))
      print("---")