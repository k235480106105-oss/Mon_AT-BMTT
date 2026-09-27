import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_message(plaintext: str, key: bytes):
    """
    Encrypt plaintext using AES-256-GCM.

    Returns:
        nonce: random 12-byte nonce
        ciphertext: encrypted data with authentication tag
    """

    aes = AESGCM(key)

    # GCM conventionally uses a 12-byte nonce.
    nonce = os.urandom(12)

    plaintext_bytes = plaintext.encode("utf-8")

    ciphertext = aes.encrypt(
        nonce,
        plaintext_bytes,
        None
    )

    return nonce, ciphertext


def decrypt_message(nonce: bytes, ciphertext: bytes, key: bytes):
    """
    Decrypt ciphertext using AES-256-GCM.
    """

    aes = AESGCM(key)

    plaintext_bytes = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext_bytes.decode("utf-8")


def main():
    print("=" * 50)
    print("       AES-256-GCM DEMONSTRATION")
    print("=" * 50)

    # AES-256 requires a 32-byte key.
    key = AESGCM.generate_key(bit_length=256)

    plaintext = "Hello! This is my Information Security project."

    print("\nPlaintext:")
    print(plaintext)

    # Encryption
    nonce, ciphertext = encrypt_message(
        plaintext,
        key
    )

    print("\nAES Key:")
    print(key.hex())

    print("\nNonce:")
    print(nonce.hex())

    print("\nCiphertext:")
    print(ciphertext.hex())

    # Decryption
    decrypted_text = decrypt_message(
        nonce,
        ciphertext,
        key
    )

    print("\nDecrypted plaintext:")
    print(decrypted_text)

    # Verification
    print("\nVerification:")

    if decrypted_text == plaintext:
        print("SUCCESS - Decryption matches original plaintext.")
    else:
        print("FAILED - Decryption does not match original plaintext.")


if __name__ == "__main__":
    main()