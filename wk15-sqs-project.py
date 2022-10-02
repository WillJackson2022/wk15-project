import boto3
client = boto3.client('sqs')

#Create a standard SQS queue for week 15 project
queue = client.create_queue(
    QueueName='Time')

#get queue url using queue name
url = client.get_queue_url(
    QueueName='Time',
)

print(url['QueueUrl'])