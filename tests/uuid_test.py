from __future__ import annotations

import uuid

from nox.domains.uuid_generator import UUIDGenerator


def test_generate_uuid1() -> None:
    generator = UUIDGenerator()
    generated_uuid = generator.generate_uuid1()

    # Check that the generated UUID is a valid UUID1
    assert isinstance(generated_uuid, str)
    parsed_uuid = uuid.UUID(generated_uuid)
    assert parsed_uuid.version == 1  # UUID1 should have version 1


def test_generate_uuid4() -> None:
    generator = UUIDGenerator()
    generated_uuid = generator.generate_uuid4()

    # Check that the generated UUID is a valid UUID4
    assert isinstance(generated_uuid, str)
    parsed_uuid = uuid.UUID(generated_uuid)
    assert parsed_uuid.version == 4  # UUID4 should have version 4


def test_uuid_uniqueness() -> None:
    generator = UUIDGenerator()

    uuid1_1 = generator.generate_uuid1()
    uuid1_2 = generator.generate_uuid1()

    uuid4_1 = generator.generate_uuid4()
    uuid4_2 = generator.generate_uuid4()

    # Ensure that each generated UUID is unique
    assert uuid1_1 != uuid1_2
    assert uuid4_1 != uuid4_2
