from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(message, key):
    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Pad the message to ensure it's a multiple of the block size
    padded_message = pad(message.encode(), DES.block_size)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(padded_message)
    
    return encrypted_message

def des_decrypt(encrypted_message, key):
    # Create a DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Decrypt the message
    decrypted_padded_message = cipher.decrypt(encrypted_message)
    
    # Unpad the decrypted message
    decrypted_message = unpad(decrypted_padded_message, DES.block_size)
    
    return decrypted_message.decode()

# Convert the key to bytes
key = b"A1B2C3D4"

# Ensure the key is 8 bytes long (64 bits) for DES
if len(key) != 8:
    print("Error: DES key must be 8 bytes long.")
    exit(1)

# Original message
message = "Confidential Data"

# Encrypt the message
encrypted = des_encrypt(message, key)
print("Encrypted Message (DES):", encrypted.hex())

# Decrypt the message
decrypted = des_decrypt(encrypted, key)
print("Decrypted Message (DES):", decrypted)
