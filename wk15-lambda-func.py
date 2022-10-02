import json
import boto3

from datetime import datetime

def lambda_handler(event, context):
 
    now = datetime.now()
    current_time = now.strftime("%H:%M %p")

    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/375507074872/The_Time",
        MessageBody=current_time
    )
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }
    