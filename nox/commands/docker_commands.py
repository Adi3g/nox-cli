from __future__ import annotations

import click

from nox.domains.docker_manager import DockerManager


@click.group()
def docker():
    """Docker management commands."""
    pass


@click.command()
@click.option('--path', required=True, help='Path to the Dockerfile or context directory')
@click.option('--tag', required=True, help='Tag for the Docker image')
def build(path, tag):
    """Build a Docker image."""
    manager = DockerManager()
    manager.build_image(path, tag)


@click.command()
@click.option('--image', required=True, help='Docker image to run')
@click.option('--name', required=True, help='Name for the running container')
@click.option('--port', multiple=True, type=(int, int), help='Port mappings (host, container)')
@click.option('--env', multiple=True, type=(str, str), help='Environment variables (KEY, VALUE)')
def run(image, name, port, env):
    """Run a Docker container."""
    ports = {f"{p[1]}/tcp": p[0] for p in port}
    env_vars = {e[0]: e[1] for e in env}
    manager = DockerManager()
    manager.run_container(image, name, ports, env_vars)


@click.command()
@click.option('--all', is_flag=True, help='List all containers, including stopped')
def list(all):
    """List Docker containers."""
    manager = DockerManager()
    manager.list_containers(all)


@click.command()
@click.option('--name', required=True, help='Name or ID of the container to stop')
def stop(name):
    """Stop a running Docker container."""
    manager = DockerManager()
    manager.stop_container(name)


@click.command()
@click.option('--name', required=True, help='Name or ID of the container to remove')
def remove(name):
    """Remove a Docker container."""
    manager = DockerManager()
    manager.remove_container(name)


@click.command()
@click.option('--image', required=True, help='Docker image to pull')
def pull(image):
    """Pull a Docker image from a registry."""
    manager = DockerManager()
    manager.pull_image(image)


@click.command()
@click.option('--image', required=True, help='Docker image to push')
def push(image):
    """Push a Docker image to a registry."""
    manager = DockerManager()
    manager.push_image(image)


# Add commands to the docker group
docker.add_command(build)
docker.add_command(run)
docker.add_command(list, name='list')
docker.add_command(stop)
docker.add_command(remove)
docker.add_command(pull)
docker.add_command(push)
