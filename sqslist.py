import boto3
# Get the service resource
sqs  = boto3.client('sqs')
# Create the queue. This returns an SQS.Queue instance
lq = sqs.list_queues(QueueNamePrefix='tmcs')
print(lq)