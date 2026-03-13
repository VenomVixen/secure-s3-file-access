import boto3

s3 = boto3.client('s3')

bucket_name = "secure-s3-project-faseeha-01"
file_name = "AWS.docx"

url = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': bucket_name,
        'Key': file_name
    },
    ExpiresIn=300
)

print("Secure temporary link:")
print(url)
