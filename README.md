# Secure S3 File Access Using Pre-Signed URLs

## Project Overview
This project demonstrates how to securely share files stored in an AWS S3 bucket using temporary pre-signed URLs.

Instead of making the S3 bucket public, the system generates a time-limited URL that allows users to download a file securely.

## Technologies Used
- Python
- AWS S3
- AWS IAM
- Boto3 SDK

## How It Works
1. A file is uploaded to an S3 bucket.
2. Python uses the Boto3 library to generate a pre-signed URL.
3. The URL allows temporary access to the file.
4. After the expiry time, the link becomes invalid.

## Security Features
- No credentials stored in the code
- IAM access control
- Temporary access using pre-signed URLs
- Secrets ignored using .gitignore

## How to Run

Install dependencies:

pip install boto3

Configure AWS CLI:

aws configure

Run the script:

python generate_link.py

## Example Output

Secure temporary link:
https://s3.amazonaws.com/your-bucket/file?AWSAccessKeyId=...

This link expires after a few minutes.
