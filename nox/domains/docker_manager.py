from __future__ import annotations

import docker
from docker.errors import APIError
from docker.errors import NotFound


class DockerManager:
    def __init__(self):
        self.client = docker.from_env()

    def build_image(self, path: str, tag: str):
        """Build a Docker image from a Dockerfile."""
        try:
            image, _ = self.client.images.build(path=path, tag=tag)
            print(f"Image {tag} built successfully.")
            return image
        except APIError as e:
            print(f"Error building image: {e}")

    def run_container(self, image: str, name: str, ports: dict):
        """Run a Docker container from an image."""
        try:
            container = self.client.containers.run(
                image, name=name, ports=ports, detach=True,
            )
            print(f"Container {name} started from image {image}.")
            return container
        except APIError as e:
            print(f"Error running container: {e}")

    def list_containers(self, all_containers: bool = False):
        """List Docker containers."""
        try:
            containers = self.client.containers.list(all=all_containers)
            for container in containers:
                print(
                    f"{container.id[:12]} - {container.name} - \
                        {container.status}",
                )
            return containers
        except APIError as e:
            print(f"Error listing containers: {e}")

    def stop_container(self, name: str):
        """Stop a running Docker container."""
        try:
            container = self.client.containers.get(name)
            container.stop()
            print(f"Container {name} stopped.")
        except NotFound:
            print(f"Container {name} not found.")
        except APIError as e:
            print(f"Error stopping container: {e}")

    def remove_container(self, name: str):
        """Remove a Docker container."""
        try:
            container = self.client.containers.get(name)
            container.remove()
            print(f"Container {name} removed.")
        except NotFound:
            print(f"Container {name} not found.")
        except APIError as e:
            print(f"Error removing container: {e}")

    def pull_image(self, image: str):
        """Pull a Docker image from Docker Hub."""
        try:
            self.client.images.pull(image)
            print(f"Image {image} pulled successfully.")
        except APIError as e:
            print(f"Error pulling image: {e}")

    def push_image(self, image: str):
        """Push a Docker image to Docker Hub."""
        try:
            self.client.images.push(image)
            print(f"Image {image} pushed successfully.")
        except APIError as e:
            print(f"Error pushing image: {e}")
