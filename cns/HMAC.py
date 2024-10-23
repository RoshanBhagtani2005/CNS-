import hashlib
import hmac

# Function to generate a cryptographic hash (e.g., using SHA-256)
def generate_hash(message, algorithm='sha256'):
    if algorithm == 'sha256':
        hash_object = hashlib.sha256(message.encode())
    elif algorithm == 'sha1':
        hash_object = hashlib.sha1(message.encode())
    elif algorithm == 'md5':
        hash_object = hashlib.md5(message.encode())
    else:
        raise ValueError("Unsupported algorithm.")
    
    # Return hexadecimal representation of the hash
    return hash_object.hexdigest()

# Function to generate HMAC using a specified cryptographic hash function
def generate_hmac(message, key, algorithm='sha256'):
    if algorithm == 'sha256':
        hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    elif algorithm == 'sha1':
        hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha1)
    elif algorithm == 'md5':
        hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.md5)
    else:
        raise ValueError("Unsupported algorithm.")
    
    # Return hexadecimal representation of the HMAC
    return hmac_obj.hexdigest()

# Demonstrating collision resistance by showing different hashes for different inputs
def demonstrate_collision_resistance(message1, message2):
    hash1 = generate_hash(message1)
    hash2 = generate_hash(message2)
    print(f"Hash of '{message1}': {hash1}")
    print(f"Hash of '{message2}': {hash2}")
    print(f"Are the hashes equal? {'Yes' if hash1 == hash2 else 'No'}")

# User Input
message = input("Enter the message: ")
key = input("Enter the key for HMAC: ")
algorithm = input("Enter the hashing algorithm (sha256/sha1/md5): ")

# Generate Cryptographic Hash
hash_value = generate_hash(message, algorithm)
print(f"Hash value of message using {algorithm}: {hash_value}")

# Generate HMAC
hmac_value = generate_hmac(message, key, algorithm)
print(f"HMAC of message using {algorithm}: {hmac_value}")

# Demonstrate Collision Resistance (Optional Example)
print("\nDemonstrating collision resistance...")
message1 = input("Enter first message for collision resistance check: ")
message2 = input("Enter second message for collision resistance check: ")
demonstrate_collision_resistance(message1, message2)
