import boto3

def upload_to_s3(file_path, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, file_path)

if __name__ == "__main__":
    file_path = "activity_report.pdf"
    bucket_name = "your-bucket-name"
    upload_to_s3(file_path, bucket_name)
