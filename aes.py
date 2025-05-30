from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt(message, key):
    # Generate a random 128-bit IV
    iv = get_random_bytes(16)
    
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the message to ensure it's a multiple of the block size
    padded_message = message.encode()
    while len(padded_message) % 16 != 0:
        padded_message += b'\x00'
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(padded_message)
    
    # Return the IV and the encrypted message
    return iv + encrypted_message

def aes_decrypt(encrypted_message, key):
    # Extract the IV from the encrypted message
    iv = encrypted_message[:16]
    encrypted_message = encrypted_message[16:]
    
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the message
    decrypted_padded_message = cipher.decrypt(encrypted_message)
    
    # Remove the padding from the decrypted message
    decrypted_message = decrypted_padded_message.decode().rstrip('\x00')
    
    return decrypted_message

# Convert the key to bytes
key = b"0123456789ABCDEF0123456789ABCDEF"

# Ensure the key is 32 bytes long (256 bits) for AES-128
if len(key) != 32:
    print("Error: AES key must be 32 bytes long.")
    exit(1)

# Original message
message = "Sensitive Information"

# Encrypt the message
encrypted = aes_encrypt(message, key)
print("Encrypted Message (AES-128):", encrypted.hex())

# Decrypt the message
decrypted = aes_decrypt(encrypted, key)
print("Decrypted Message (AES-128):", decrypted)
