from __future__ import annotations

import docker
from docker.errors import DockerException


class DockerManager:
    def __init__(self):
        self.client = docker.from_env()

    def build_image(self, path: str, tag: str) -> None:
        """Build a Docker image from a specified path."""
        try:
            image, logs = self.client.images.build(path=path, tag=tag)
            for log in logs:
                print(log.get('stream', '').strip())
            print(f"Image {tag} built successfully.")
        except DockerException as e:
            print(f"Error building image: {e}")

    def run_container(
        self, image: str, name: str, ports: dict, env_vars: dict[str, str] | None = None,
    ) -> None:
        """Run a Docker container from an image."""
        try:
            self.client.containers.run(
                image, name=name, ports=ports, environment=env_vars, detach=True,
            )
            print(f"Container {name} running.")
        except DockerException as e:
            print(f"Error running container: {e}")

    def list_containers(self, all_containers: bool = False) -> None:
        """List all Docker containers."""
        containers = self.client.containers.list(all=all_containers)
        for container in containers:
            print(f"ID: {container.id}, Name: {container.name}, Status: {container.status}")

    def stop_container(self, name: str) -> None:
        """Stop a running Docker container."""
        try:
            container = self.client.containers.get(name)
            container.stop()
            print(f"Container {name} stopped.")
        except DockerException as e:
            print(f"Error stopping container: {e}")

    def remove_container(self, name: str) -> None:
        """Remove a Docker container."""
        try:
            container = self.client.containers.get(name)
            container.remove(force=True)
            print(f"Container {name} removed.")
        except DockerException as e:
            print(f"Error removing container: {e}")

    def pull_image(self, image: str) -> None:
        """Pull a Docker image from a registry."""
        try:
            self.client.images.pull(image)
            print(f"Image {image} pulled successfully.")
        except DockerException as e:
            print(f"Error pulling image: {e}")

    def push_image(self, image: str) -> None:
        """Push a Docker image to a registry."""
        try:
            self.client.images.push(image)
            print(f"Image {image} pushed successfully.")
        except DockerException as e:
            print(f"Error pushing image: {e}")
