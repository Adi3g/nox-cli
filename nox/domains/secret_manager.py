from __future__ import annotations

import boto3
from botocore.exceptions import ClientError


class SecretsManager:
    def __init__(self, region_name=None):
        self.client = boto3.client('secretsmanager', region_name=region_name)

    def store_secret(self, name: str, value: str):
        """Store a secret in AWS Secrets Manager."""
        try:
            self.client.create_secret(Name=name, SecretString=value)
            print(f"Secret {name} stored successfully.")
        except ClientError as e:
            print(f"Error storing secret {name}: {e}")

    def get_secret(self, name: str) -> str:
        """Retrieve a secret from AWS Secrets Manager."""
        try:
            response = self.client.get_secret_value(SecretId=name)
            return response['SecretString']
        except ClientError as e:
            print(f"Error retrieving secret {name}: {e}")
            return ''

    def list_secrets(self):
        """List secrets in AWS Secrets Manager."""
        try:
            response = self.client.list_secrets()
            secrets = response.get('SecretList', [])
            for secret in secrets:
                print(f"Name: {secret['Name']}")
        except ClientError as e:
            print(f"Error listing secrets: {e}")

    def delete_secret(self, name: str):
        """Delete a secret from AWS Secrets Manager."""
        try:
            self.client.delete_secret(
                SecretId=name, ForceDeleteWithoutRecovery=True,
            )
            print(f"Secret {name} deleted successfully.")
        except ClientError as e:
            print(f"Error deleting secret {name}: {e}")
