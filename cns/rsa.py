import random
from sympy import isprime
from math import gcd

# Helper function to compute modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to calculate the greatest common divisor
def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Generate RSA Keys
def generate_rsa_keys(p, q):
    if not (isprime(p) and isprime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be the same.')

    # Step 1: Calculate n = p * q
    n = p * q

    # Step 2: Calculate the totient φ(n) = (p-1)(q-1)
    phi = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.randrange(2, phi)
    while compute_gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Step 4: Compute d such that (d * e) % φ(n) = 1 (modular inverse of e mod φ(n))
    d = modinv(e, phi)

    # Public and Private keys
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# Encryption
def encrypt(plaintext, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Decryption
def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# User Input
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

public_key, private_key = generate_rsa_keys(p, q)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Encryption
message = input("Enter the message to encrypt: ")
ciphertext = encrypt(message, public_key)
print(f"Ciphertext: {ciphertext}")

# Decryption
decrypted_message = decrypt(ciphertext, private_key)
print(f"Decrypted message: {decrypted_message}")
