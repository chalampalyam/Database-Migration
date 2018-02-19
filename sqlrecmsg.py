import boto3

sqsclient  = boto3.resource('sqs')

queue = sqsclient.Queue('https://sqs.ap-south-1.amazonaws.com/071117670759/tmcsQ1')

msg = queue.receive_messages(MaxNumberOfMessages=2,WaitTimeSeconds=10)
                 

print(msg)




