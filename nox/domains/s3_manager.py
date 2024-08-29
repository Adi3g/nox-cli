from __future__ import annotations

import os

import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError


class S3Manager:
    def __init__(
        self, aws_access_key_id=None, aws_secret_access_key=None,
        region_name=None,
    ):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )

    def list_objects(self, bucket_name):
        """List objects in an S3 bucket."""
        try:
            response = self.s3.list_objects_v2(Bucket=bucket_name)
            return response.get('Contents', [])
        except ClientError as e:
            print(f"Error listing objects in bucket {bucket_name}: {e}")
            return []

    def upload_file(self, bucket_name, file_path, object_name=None):
        """Upload a file to an S3 bucket."""
        try:
            # Use the provided object_name or default to the file's base name
            object_name = object_name or os.path.basename(file_path)
            self.s3.upload_file(file_path, bucket_name, object_name)
            print(f"File {file_path} uploaded to {bucket_name}/{object_name}.")
        except NoCredentialsError:
            print('AWS credentials not found.')
        except ClientError as e:
            print(f"Error uploading file to bucket {bucket_name}: {e}")

    def download_file(self, bucket_name, object_name, output_path):
        """Download a file from an S3 bucket."""
        try:
            self.s3.download_file(bucket_name, object_name, output_path)
            print(
                f"File {object_name} downloaded from {bucket_name} \
                    to {output_path}.",
            )
        except NoCredentialsError:
            print('AWS credentials not found.')
        except ClientError as e:
            print(f"Error downloading file from bucket {bucket_name}: {e}")

    def delete_object(self, bucket_name, object_name):
        """Delete an object from an S3 bucket."""
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)
            print(f"Object {object_name} deleted from bucket {bucket_name}.")
        except ClientError as e:
            print(f"Error deleting object from bucket {bucket_name}: {e}")
