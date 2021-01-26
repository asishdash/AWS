import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('usersTest')

def lambda_handler(event, context):
    table.put_item(
	Item = {
		'id': '1234578',
                'temp' : 'too hot'
	}
    )
    response = {
	'message': 'Item added'
    }
    return {
        'statusCode': 200,
        'body': response
    }