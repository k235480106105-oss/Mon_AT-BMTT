from math import gcd


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.

    Returns:
        gcd, x, y
    such that:
        a*x + b*y = gcd(a, b)
    """

    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


def modular_inverse(e, phi):
    """
    Calculate modular inverse of e modulo phi.

    Find d such that:
        e * d ≡ 1 (mod phi)
    """

    gcd_value, x, _ = extended_gcd(e, phi)

    if gcd_value != 1:
        raise ValueError(
            "e and phi(n) must be coprime."
        )

    return x % phi


def generate_rsa_keys(p, q):
    """
    Generate RSA public and private keys
    from two prime numbers p and q.

    This function is for educational demonstration.
    """

    # Step 1: Calculate n
    n = p * q

    # Step 2: Calculate Euler's totient
    phi = (p - 1) * (q - 1)

    # Step 3: Choose public exponent e
    e = 17

    if gcd(e, phi) != 1:
        raise ValueError(
            "e and phi(n) must be coprime."
        )

    # Step 4: Calculate private exponent d
    d = modular_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key, phi


def main():
    print("=" * 60)
    print("              RSA KEY GENERATION DEMO")
    print("=" * 60)

    # Small numbers are used only for demonstration.
    p = 61
    q = 53

    print(f"\np = {p}")
    print(f"q = {q}")

    public_key, private_key, phi = generate_rsa_keys(
        p,
        q
    )

    e, n = public_key
    d, _ = private_key

    print(f"\nn = p * q = {n}")

    print(f"\nphi(n) = {phi}")

    print(f"\nPublic exponent e = {e}")

    print(f"\nPrivate exponent d = {d}")

    print("\nPublic Key:")
    print(public_key)

    print("\nPrivate Key:")
    print(private_key)

    # Verify the relationship between e and d.
    verification = (e * d) % phi

    print("\nVerification:")
    print(f"(e * d) mod phi(n) = {verification}")

    if verification == 1:
        print("SUCCESS - RSA key generation is valid.")
    else:
        print("FAILED - RSA key generation is invalid.")


if __name__ == "__main__":
    main()