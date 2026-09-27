from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_rsa_key_pair():
    """
    Generate RSA-2048 public/private key pair.
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def hybrid_encrypt(message, receiver_public_key):
    """
    Encrypt message using hybrid encryption.

    AES-256-GCM encrypts the actual message.
    RSA-OAEP encrypts the AES key.
    """

    # Generate random AES-256 key
    aes_key = AESGCM.generate_key(bit_length=256)

    # Create AES cipher
    aes = AESGCM(aes_key)

    # Generate 12-byte nonce
    nonce = __import__("secrets").token_bytes(12)

    # Encrypt message using AES-GCM
    ciphertext = aes.encrypt(
        nonce,
        message.encode("utf-8"),
        None
    )

    # Encrypt AES key using receiver's RSA public key
    encrypted_aes_key = receiver_public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_aes_key, nonce, ciphertext


def hybrid_decrypt(
    encrypted_aes_key,
    nonce,
    ciphertext,
    receiver_private_key
):
    """
    Decrypt hybrid-encrypted message.
    """

    # Recover AES key using RSA private key
    aes_key = receiver_private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt message using recovered AES key
    aes = AESGCM(aes_key)

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode("utf-8")


def main():
    print("=" * 70)
    print("             RSA + AES HYBRID ENCRYPTION")
    print("=" * 70)

    # Receiver: Bob
    bob_private_key, bob_public_key = generate_rsa_key_pair()

    message = (
        "This is a secret message protected by "
        "AES-256-GCM and RSA-2048-OAEP."
    )

    print("\nOriginal message:")
    print(message)

    # Alice encrypts message for Bob
    encrypted_aes_key, nonce, ciphertext = hybrid_encrypt(
        message,
        bob_public_key
    )

    print("\nEncrypted AES key:")
    print(encrypted_aes_key.hex())

    print("\nNonce:")
    print(nonce.hex())

    print("\nCiphertext:")
    print(ciphertext.hex())

    # Bob decrypts the message
    decrypted_message = hybrid_decrypt(
        encrypted_aes_key,
        nonce,
        ciphertext,
        bob_private_key
    )

    print("\nDecrypted message:")
    print(decrypted_message)

    print("\nVerification:")

    if decrypted_message == message:
        print(
            "SUCCESS - Hybrid encryption/decryption "
            "completed successfully."
        )
    else:
        print("FAILED - Decrypted message does not match.")


if __name__ == "__main__":
    main()