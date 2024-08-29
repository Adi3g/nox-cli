from __future__ import annotations

import click

from nox.domains.s3_manager import S3Manager


@click.group()
def s3():
    """S3 commands for managing AWS S3 buckets."""
    pass


@click.command()
@click.option('--bucket', required=True, help='Name of the S3 bucket')
def list(bucket):
    """List objects in an S3 bucket."""
    manager = S3Manager()
    objects = manager.list_objects(bucket)
    if objects:
        for obj in objects:
            click.echo(f"{obj['Key']} ({obj['Size']} bytes)")
    else:
        click.echo(f"No objects found in bucket {bucket}.")


@click.command()
@click.option('--bucket', required=True, help='Name of the S3 bucket')
@click.option(
    '--file', 'file_path', required=True,
    help='Path to the file to upload',
)
@click.option(
    '--object', 'object_name', default=None,
    help='S3 object name (defaults to file name)',
)
def upload(bucket, file_path, object_name):
    """Upload a file to an S3 bucket."""
    manager = S3Manager()
    manager.upload_file(bucket, file_path, object_name)


@click.command()
@click.option('--bucket', required=True, help='Name of the S3 bucket')
@click.option(
    '--file', 'object_name', required=True,
    help='S3 object name to download',
)
@click.option(
    '--output', required=True,
    help='Path to save the downloaded file',
)
def download(bucket, object_name, output):
    """Download a file from an S3 bucket."""
    manager = S3Manager()
    manager.download_file(bucket, object_name, output)


@click.command()
@click.option('--bucket', required=True, help='Name of the S3 bucket')
@click.option(
    '--file', 'object_name', required=True,
    help='S3 object name to delete',
)
def delete(bucket, object_name):
    """Delete an object from an S3 bucket."""
    manager = S3Manager()
    manager.delete_object(bucket, object_name)


# Add commands to the s3 group
s3.add_command(list, name='list')
s3.add_command(upload, name='upload')
s3.add_command(download, name='download')
s3.add_command(delete, name='delete')
