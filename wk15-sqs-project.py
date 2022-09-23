import boto3
client = boto3.client('sqs')

queue = client.create_queue(QueueName='The_Time')

url = client.get_queue_url(QueueName='The_Time')

print(url['QueueUrl'])