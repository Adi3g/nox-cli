# Nox

Nox is a Python CLI tool designed to automate and streamline various day-to-day tasks commonly performed by software engineers. It provides functionalities like JWT management, encryption/decryption, interaction with AWS S3, database operations, Docker management, and more.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [JWT Management](#jwt-management)
  - [Encryption and Decryption](#encryption-and-decryption)
  - [S3 File Management](#s3-file-management)
  - [Database Operations](#database-operations)
  - [Docker Management](#docker-management)
  - [Network Operations](#network-operations)
  - [Secrets Management](#secrets-management)
  - [File and Directory Operations](#file-and-directory-operations)
  - [UUID Generation](#uuid-generation)
  - [Weather Plugin](#weather-plugin)
- [Plugins](#plugins)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **JWT Management**: Generate and verify JWT tokens for different environments.
- **Encryption/Decryption**: Encrypt and decrypt text or files using various algorithms.
- **S3 File Management**: List, upload, and remove files from AWS S3 buckets.
- **Database Operations**: Run queries and manage database migrations.
- **Docker Management**: Build and run Docker containers with ease.
- **Network Operations**: Perform network-related tasks like ping, traceroute, and DNS lookups.
- **Secrets Management**: Store and retrieve secrets securely.
- **File and Directory Operations**: Search for files, calculate directory sizes, and more.
- **UUID Generation**: Generate UUIDs for various purposes.
- **Extensible**: Easily add new commands and features through plugins.

## Usage

Nox provides a variety of commands. Here are some examples:

### JWT Management

Generate a JWT for a specific environment:

```bash
nox jwt generate --env prod --key /path/to/key.pem --claims claims.json
```

Verify a JWT token:

```bash
nox jwt verify --token your.jwt.token --key /path/to/public.pem
```

### Encryption and Decryption

Encrypt a file using AES encryption:

```bash
nox encrypt --input secret.txt --output secret.enc --key /path/to/key.pem --type AES
```

Decrypt a file:

```bash
nox decrypt --input secret.enc --output secret.txt --key /path/to/key.pem
```

### S3 File Management

List files in an S3 bucket:

```bash
nox s3 list --bucket my-bucket --region us-west-2
```

Upload a file to S3:

```bash
nox s3 add --file report.csv --bucket my-bucket --region us-west-2
```

Remove a file from S3:

```bash
nox s3 remove --file report.csv --bucket my-bucket --region us-west-2
```

### Database Operations

Run a SQL query on a PostgreSQL database:

```bash
nox db query --db "postgresql://user:password@localhost:5432/mydb" --query "SELECT * FROM users"
```

Migrate a database:

```bash
nox db migrate --db "postgresql://user:password@localhost:5432/mydb" --migration migrations.sql
```

### Docker Management

Build a Docker image:

```bash
nox docker build --tag my-image:latest --file Dockerfile
```

Run a Docker container:

```bash
nox docker run --tag my-image:latest --env .env --ports "8080:80"
```

### Network Operations

Ping a host:

```bash
nox net ping --host google.com
```

Perform a traceroute:

```bash
nox net traceroute --host google.com
```

Perform a DNS lookup:

```bash
nox net dns --domain example.com
```

### Secrets Management

Retrieve a secret from AWS Secrets Manager:

```bash
nox secrets get --name my-secret --region us-west-2
```

Store a new secret in AWS Secrets Manager:

```bash
nox secrets store --name my-secret --value "super-secret-value" --region us-west-2
```

### File and Directory Operations

Search for files matching a pattern:

```bash
nox file search --path /path/to/directory --pattern "*.log"
```

Calculate the size of a directory:

```bash
nox file size --path /path/to/directory
```

### UUID Generation

Generate a new UUID:

```bash
nox uuid generate
```

### Weather Plugin

The Weather Plugin adds a command to check the current weather for a specified location.

#### Usage

```bash
nox weather "New York"
```

This will output the current weather in New York, based on mock data:

```bash
The current weather in New York is Sunny, 25°C.
```

#### Note

This is a mock implementation. You can extend it by integrating with a real weather API.

## Plugins

Nox supports a plugin system that allows you to extend its functionality without modifying the core codebase.

### Creating a Plugin

To create a plugin, follow these steps:

1. Create a new Python file in the `nox/plugins/` directory.
2. Implement the `NoxPlugin` interface.

```python
# nox/plugins/my_plugin.py

import click
from nox.plugins import NoxPlugin

class MyPlugin(NoxPlugin):
    def register_commands(self, cli):
        @cli.command()
        def my_command():
            """Command provided by MyPlugin."""
            click.echo("This is a command from MyPlugin!")

plugin = MyPlugin()
```

3. Your plugin will be automatically discovered and loaded when you run Nox.

### Loading External Plugins

To load plugins distributed as separate packages, ensure they are installed in the same environment as Nox, and they will be discovered automatically.

## Configuration

Nox can be configured via a `.noxconfig` file or environment variables. Below is an example `.noxconfig` file:

```json
{
  "jwt": {
    "default_env": "dev"
  },
  "s3": {
    "default_region": "us-west-2"
  },
  "db": {
    "default_connection_string": "postgresql://user:password@localhost:5432/mydb"
  },
  "secrets": {
    "default_region": "us-west-2"
  }
}
```

Place this file in your project's root directory, and Nox will automatically use these settings.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Before contributing, please ensure you have read the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
