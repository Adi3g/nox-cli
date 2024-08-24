from __future__ import annotations

import uuid


class UUIDGenerator:
    @staticmethod
    def generate_uuid1() -> str:
        """Generate a UUID based on the host ID and current time."""
        return str(uuid.uuid1())

    @staticmethod
    def generate_uuid4() -> str:
        """Generate a random UUID."""
        return str(uuid.uuid4())
