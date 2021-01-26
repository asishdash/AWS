import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/116263928116/LambdaDemo'


def lambda_handler(event, context):
    # Send message to SQS queue

    entries = []
    for i in range(1, 10):
        entry = {
            'Id': 'id%s' % str(i),
            'MessageBody': str(i)
        }
        entries.append(entry)

    response = response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            str(entries)
        )
    )

    print(response['MessageId'])