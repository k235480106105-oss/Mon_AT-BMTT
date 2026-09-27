import pytest
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from src.aes_demo import encrypt_message, decrypt_message


def test_encrypt_decrypt():
    """
    Test cơ bản:
    Plaintext -> Encrypt -> Decrypt -> Plaintext
    """

    key = AESGCM.generate_key(bit_length=256)

    plaintext = "Information Security Project"

    nonce, ciphertext = encrypt_message(
        plaintext,
        key
    )

    decrypted = decrypt_message(
        nonce,
        ciphertext,
        key
    )

    assert decrypted == plaintext


def test_wrong_key():
    """
    Giải mã bằng key khác phải thất bại.
    """

    key = AESGCM.generate_key(bit_length=256)
    wrong_key = AESGCM.generate_key(bit_length=256)

    plaintext = "Secret information"

    nonce, ciphertext = encrypt_message(
        plaintext,
        key
    )

    with pytest.raises(Exception):
        decrypt_message(
            nonce,
            ciphertext,
            wrong_key
        )


def test_modified_ciphertext():
    """
    Nếu ciphertext bị thay đổi,
    AES-GCM phải phát hiện và từ chối giải mã.
    """

    key = AESGCM.generate_key(bit_length=256)

    plaintext = "Important information"

    nonce, ciphertext = encrypt_message(
        plaintext,
        key
    )

    # Chuyển ciphertext sang bytearray để có thể thay đổi 1 byte.
    modified_ciphertext = bytearray(ciphertext)

    # Thay đổi một bit trong ciphertext.
    modified_ciphertext[0] ^= 1

    with pytest.raises(Exception):
        decrypt_message(
            nonce,
            bytes(modified_ciphertext),
            key
        )