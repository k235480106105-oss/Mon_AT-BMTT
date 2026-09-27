import time

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


ITERATIONS = 100


def benchmark_aes(data):
    key = AESGCM.generate_key(bit_length=256)
    nonce = b"123456789012"
    aes = AESGCM(key)

    encryption_times = []
    decryption_times = []

    ciphertext = None

    for _ in range(ITERATIONS):
        start = time.perf_counter()

        ciphertext = aes.encrypt(
            nonce,
            data,
            None
        )

        encryption_times.append(
            time.perf_counter() - start
        )

    for _ in range(ITERATIONS):
        start = time.perf_counter()

        aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        decryption_times.append(
            time.perf_counter() - start
        )

    average_encryption = sum(encryption_times) / ITERATIONS
    average_decryption = sum(decryption_times) / ITERATIONS

    return average_encryption, average_decryption


def benchmark_rsa(data, private_key, public_key):
    encryption_times = []
    decryption_times = []

    ciphertext = None

    for _ in range(ITERATIONS):
        start = time.perf_counter()

        ciphertext = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        encryption_times.append(
            time.perf_counter() - start
        )

    for _ in range(ITERATIONS):
        start = time.perf_counter()

        private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        decryption_times.append(
            time.perf_counter() - start
        )

    average_encryption = sum(encryption_times) / ITERATIONS
    average_decryption = sum(decryption_times) / ITERATIONS

    return average_encryption, average_decryption


def main():
    print("=" * 70)
    print("          AES vs RSA PERFORMANCE BENCHMARK")
    print("=" * 70)

    print(f"\nNumber of iterations: {ITERATIONS}")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    # AES benchmark
    print("\nAES-256-GCM:")

    for size in [
        1024,
        10 * 1024,
        100 * 1024,
        1024 * 1024
    ]:

        data = b"A" * size

        enc, dec = benchmark_aes(data)

        print(
            f"{size:>10} bytes | "
            f"Encrypt: {enc:.8f} s | "
            f"Decrypt: {dec:.8f} s"
        )

    # RSA benchmark
    print("\nRSA-2048-OAEP:")

    for size in [32, 64, 128]:

        data = b"A" * size

        enc, dec = benchmark_rsa(
            data,
            private_key,
            public_key
        )

        print(
            f"{size:>10} bytes | "
            f"Encrypt: {enc:.8f} s | "
            f"Decrypt: {dec:.8f} s"
        )

    print("\nConclusion:")
    print(
        "AES is suitable for encrypting large amounts of data."
    )
    print(
        "RSA is computationally more expensive and is "
        "not suitable for direct large-data encryption."
    )


if __name__ == "__main__":
    main()