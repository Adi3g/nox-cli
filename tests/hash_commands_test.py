from __future__ import annotations

import pytest

from nox.domains.hash_manager import HashManager


@pytest.fixture
def hash_manager():
    return HashManager()


def test_generate_hash_md5(hash_manager, tmp_path):
    test_file = tmp_path / 'test.txt'
    test_file.write_text('This is a test file.')
    file_hash = hash_manager.generate_hash(str(test_file), algorithm='md5')
    assert file_hash == '3de8f8b0dc94b8c2230fab9ec0ba0506', \
        'MD5 hash mismatch.'


def test_generate_hash_sha256(hash_manager, tmp_path):
    test_file = tmp_path / 'test.txt'
    test_file.write_text('This is a test file.')
    file_hash = hash_manager.generate_hash(str(test_file), algorithm='sha256')
    assert file_hash == \
        'f29bc64a9d3732b4b9035125fdb3285f5b6455778edca72414671e0ca3b2e0de', \
        'SHA256 hash mismatch.'


def test_verify_hash(hash_manager, tmp_path):
    test_file = tmp_path / 'test.txt'
    test_file.write_text('This is a test file.')
    assert hash_manager.verify_hash(
        str(
            test_file,
        ), '3de8f8b0dc94b8c2230fab9ec0ba0506', 'md5',
    ), 'Hash verification failed.'
    assert not hash_manager.verify_hash(
        str(test_file), 'wronghashvalue', 'md5',
    ), 'Hash verification should fail.'
