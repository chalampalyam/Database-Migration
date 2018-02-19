import boto3
# Get the service resource
sqs  = boto3.client('sqs')
# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='tmcs_sqstest', \
    Attributes={'DelaySeconds': '5'})
print(queue)
