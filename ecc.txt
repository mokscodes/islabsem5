// ECC
import random

# Simple implementation of ECC parameters
def generate_keys():
    # Private key
    private_key = random.randint(1, 100)  # Random private key
    # Public key (for simplicity, public key is a scalar multiple of the base point)
    public_key = (private_key * G[0] % p, private_key * G[1] % p)
    return private_key, public_key

# 8)ECC parameters (for the sake of the example)
p = 191  # A prime number (the field size)
G = (5, 10)  # Base point (G)

def encrypt(public_key, message):
    k = random.randint(1, 20)  # Random k, keep it small for simplicity
    # Encrypt the message
    encrypted_message = []
    for char in message:
        # Encrypt using a simple method: XOR with a key
        encrypted_char = (ord(char) + (k + public_key[0])) % 256
        encrypted_message.append(encrypted_char)
    return encrypted_message, k  # Return k for decryption

def decrypt(private_key, encrypted_message, k):
    # Decrypt the message
    decrypted_message = []
    for encrypted_char in encrypted_message:
        # Decrypt by reversing the encryption process
        decrypted_char = chr((encrypted_char - (k + private_key * G[0])) % 256)
        decrypted_message.append(decrypted_char)
    return ''.join(decrypted_message)

# Generate keys
private_key, public_key = generate_keys()

# Original message
original_message = "Secure Transactions"  # The message to encrypt

# Encrypt the message
ciphertext, k = encrypt(public_key, original_message)

# Decrypt the ciphertext
decrypted_message = decrypt(private_key, ciphertext, k)

# Output results
print("Ciphertext (encrypted message):", ciphertext)
print("Decrypted message (should match original):", decrypted_message)
