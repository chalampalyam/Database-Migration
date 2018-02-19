#Import required pacakges
import boto3

#Create S3 client
s3client = boto3.client('s3')

# Declare Variablese
bucketName = 's3lambdainput'
inputfile   = 'sqllist.py'
outputfile = sqllistcopy2
.py

#Step1: Get file from S3
s3file = s3client.get_object(Bucket=bucketName,Key=inputfile)

#Step2: Read the inputfile
records = (s3file['Body'].read())


#Step3: Create outputfile using recrods from input file
putrespose = s3client.put_object(Bucket=bucket,Key=outputfile,Body=records)

print(putrespose)
print('program end successfully')


