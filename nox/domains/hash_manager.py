from __future__ import annotations

import hashlib


class HashManager:
    def generate_hash(self, file_path: str, algorithm: str = 'md5') -> str:
        """Generate a hash for the given file using the specified algorithm."""
        hash_func = getattr(hashlib, algorithm)()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return ''
        except Exception as e:
            print(f"Error generating hash: {e}")
            return ''

    def verify_hash(
        self, file_path: str,
        expected_hash: str, algorithm: str = 'md5',
    ) -> bool:
        """Verify the hash of the given file against the expected hash."""
        actual_hash = self.generate_hash(file_path, algorithm)
        return actual_hash == expected_hash
