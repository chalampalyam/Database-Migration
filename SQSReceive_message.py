import boto3
sqsclient = boto3.client('sqs')

recmsg = sqsclient.receive_message(QueueUrl ='https://sqs.ap-south-1.amazonaws.com/071117670759/tmcsQ1',MaxNumberOfMessages=10)
print(recmsg)
messages = recmsg['Messages']

print(messages[0]['Body'])






