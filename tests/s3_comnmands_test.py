from __future__ import annotations

import boto3
import pytest
from moto import mock_aws

from nox.domains.s3_manager import S3Manager


@pytest.fixture
def s3_client():
    with mock_aws():
        # Initialize mock S3 service
        boto3.client('s3').create_bucket(Bucket='test-bucket')
        yield S3Manager()


def test_list_objects_empty(s3_client):
    """Test listing objects in an empty bucket."""
    objects = s3_client.list_objects('test-bucket')
    assert objects == [], 'Expected no objects in the bucket.'


def test_upload_file(s3_client, tmp_path):
    """Test uploading a file to S3."""
    # Create a temporary file
    test_file = tmp_path / 'test.txt'
    test_file.write_text('This is a test file.')

    # Upload the file
    s3_client.upload_file('test-bucket', str(test_file))

    # Verify the file is uploaded
    objects = s3_client.list_objects('test-bucket')
    assert len(objects) == 1, 'Expected one object in the bucket.'
    assert objects[0]['Key'] == 'test.txt', \
        "Expected the object key to be 'test.txt'."


def test_download_file(s3_client, tmp_path):
    """Test downloading a file from S3."""
    # Upload a file to S3 first
    test_file = tmp_path / 'test.txt'
    test_file.write_text('This is a test file.')
    s3_client.upload_file(
        'test-bucket', str(test_file),
        object_name='test.txt',
    )  # Ensure object name matches

    # Download the file
    output_file = tmp_path / 'downloaded.txt'
    s3_client.download_file('test-bucket', 'test.txt', str(output_file))

    # Verify the file content
    assert output_file.read_text(
    ) == 'This is a test file.', 'Downloaded file content mismatch.'


def test_delete_object(s3_client):
    """Test deleting an object from S3."""
    # Upload a file to S3 first
    s3_client.upload_file('test-bucket', __file__, object_name='test.txt')

    # Delete the file
    s3_client.delete_object('test-bucket', 'test.txt')

    # Verify the file is deleted
    objects = s3_client.list_objects('test-bucket')
    assert len(objects) == 0, \
        'Expected no objects in the bucket after deletion.'
