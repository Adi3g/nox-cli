from __future__ import annotations

import base64

import rsa
from cryptography.fernet import Fernet


class EncryptionManager:
    def __init__(
        self, input_text=None, input_file=None,
        output_file=None, key_file=None,
    ):
        self.input_text = input_text
        self.input_file = input_file
        self.output_file = output_file

        if key_file:
            with open(key_file, 'rb') as file:
                self.key = file.read()

    def encrypt_fernet(self) -> bytes:
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(
            self.input_text.encode(
            ),
        ) if self.input_text else fernet.encrypt(self.input_file.read())
        return encrypted_data

    def decrypt_fernet(self) -> bytes:
        fernet = Fernet(self.key)
        decrypted_data = fernet.decrypt(
            self.input_text.encode(
            ),
        ) if self.input_text else fernet.decrypt(self.input_file.read())
        return decrypted_data

    def encrypt_base64(self) -> bytes:
        encrypted_data = base64.b64encode(
            self.input_text.encode(
            ),
        ) if self.input_text else base64.b64encode(self.input_file.read())
        return encrypted_data

    def decrypt_base64(self) -> bytes:
        decrypted_data = base64.b64decode(
            self.input_text.encode(
            ),
        ) if self.input_text else base64.b64decode(self.input_file.read())
        return decrypted_data

    def encrypt_rsa(self) -> bytes:
        public_key = rsa.PublicKey.load_pkcs1_openssl_pem(self.key)
        encrypted_data = rsa.encrypt(
            self.input_text.encode(
            ), public_key,
        ) if self.input_text else rsa.encrypt(
            self.input_file.read(),
            public_key,
        )
        return encrypted_data

    def decrypt_rsa(self) -> bytes:
        private_key = rsa.PrivateKey.load_pkcs1(self.key)
        decrypted_data = rsa.decrypt(
            self.input_text.encode(
            ), private_key,
        ) if self.input_text else rsa.decrypt(
            self.input_file.read(),
            private_key,
        )
        return decrypted_data
