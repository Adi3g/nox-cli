from __future__ import annotations

from typing import Any

import redis


class RedisManager:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        """Initialize the Redis manager."""
        self.client = redis.Redis(host=host, port=port, db=db)

    def set_key(self, key: str, value: Any) -> str:
        """Set a key in Redis."""
        try:
            self.client.set(key, value)
            return f"Key '{key}' set successfully."
        except Exception as e:
            return f"Error setting key '{key}': {str(e)}"

    def get_key(self, key: str) -> str | None:
        """Get a key from Redis."""
        try:
            value = self.client.get(key)
            return value.decode() if value else 'Key not found.'
        except Exception as e:
            return f"Error getting key '{key}': {str(e)}"

    def delete_key(self, key: str) -> str:
        """Delete a key from Redis."""
        try:
            self.client.delete(key)
            return f"Key '{key}' deleted successfully."
        except Exception as e:
            return f"Error deleting key '{key}': {str(e)}"

    def list_keys(self, pattern: str = '*') -> list[str]:
        """List keys in Redis matching a pattern."""
        try:
            keys = self.client.keys(pattern)
            return [key.decode() for key in keys]
        except Exception as e:
            return [f"Error listing keys: {str(e)}"]

    def flush_database(self) -> str:
        """Flush the current database."""
        try:
            self.client.flushdb()
            return 'Database flushed successfully.'
        except Exception as e:
            return f"Error flushing database: {str(e)}"

    def info(self) -> str:
        """Get Redis server info."""
        try:
            info = self.client.info()
            return '\n'.join([f"{k}: {v}" for k, v in info.items()])
        except Exception as e:
            return f"Error retrieving server info: {str(e)}"
