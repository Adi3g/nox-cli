from __future__ import annotations

import os

from dotenv import load_dotenv
from dotenv import set_key
from dotenv import unset_key


class EnvManager:
    def __init__(self, env_file: str = '.env'):
        self.env_file = env_file
        load_dotenv(self.env_file)

    def load_env_file(self, file_path: str):
        """Load environment variables from a specified file."""
        load_dotenv(file_path)
        print(f"Environment variables loaded from {file_path}.")

    def set_env_variable(self, key: str, value: str):
        """Set an environment variable."""
        os.environ[key] = value
        set_key(self.env_file, key, value)
        print(f"Environment variable {key} set to {value}.")

    def get_env_variable(self, key: str) -> str:
        """Get the value of an environment variable."""
        return os.getenv(key, '')

    def unset_env_variable(self, key: str):
        """Unset an environment variable."""
        os.environ.pop(key, None)
        unset_key(self.env_file, key)
        print(f"Environment variable {key} removed.")

    def list_env_variables(self):
        """List all environment variables."""
        for key, value in os.environ.items():
            print(f"{key}: {value}")
