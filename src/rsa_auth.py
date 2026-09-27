from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_key_pair():
    """
    Generate an RSA-2048 key pair.
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def sign_message(message, private_key):
    """
    Create an RSA-PSS digital signature.
    """

    signature = private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature


def verify_signature(message, signature, public_key):
    """
    Verify an RSA-PSS digital signature.
    """

    try:
        public_key.verify(
            signature,
            message.encode("utf-8"),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return True

    except Exception:
        return False


def main():
    print("=" * 60)
    print("             RSA DIGITAL SIGNATURE DEMO")
    print("=" * 60)

    # Alice's key pair
    alice_private_key, alice_public_key = generate_key_pair()

    message = "This message is from Alice."

    print("\nOriginal message:")
    print(message)

    # Alice signs the message
    signature = sign_message(
        message,
        alice_private_key
    )

    print("\nSignature:")
    print(signature.hex())

    # Bob verifies Alice's signature
    valid = verify_signature(
        message,
        signature,
        alice_public_key
    )

    print("\nVerification:")

    if valid:
        print("SUCCESS - Signature is valid.")
        print("The message was signed by the owner of Alice's private key.")
    else:
        print("FAILED - Signature is invalid.")

    # Test modified message
    modified_message = "This message has been modified."

    modified_valid = verify_signature(
        modified_message,
        signature,
        alice_public_key
    )

    print("\nModified message verification:")

    if modified_valid:
        print("FAILED - Modified message was accepted.")
    else:
        print("SUCCESS - Modified message was rejected.")


if __name__ == "__main__":
    main()