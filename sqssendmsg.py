import boto3

client  = boto3.client('sqs')

qurl = 'https://sqs.ap-south-1.amazonaws.com/071117670759/tmcsQ1'
body = "INSERT INTO Cars VALUES(1,'Audi',52642)"
dsecs = 1

msg = client.send_message(QueueUrl=qurl,
        MessageBody=body,
        DelaySeconds=dsecs)

print(msg)
