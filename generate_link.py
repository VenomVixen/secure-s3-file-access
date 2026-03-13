import boto3

# Create S3 client (uses credentials from AWS CLI config)
s3 = boto3.client('s3')

bucket_name = "YOUR_BUCKET_NAME" # Replace with your actual bucket name
file_name = "YOUR_FILE_NAME" # Replace with the actual file name you want to generate a link for

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
