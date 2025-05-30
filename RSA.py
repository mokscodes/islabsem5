def encrypt_rsa(message, n, e):
    # Encrypt the message
    encrypted_message = []
    for char in message:
        # Convert character to its ASCII value, then encrypt using RSA
        encrypted_char = (ord(char) ** e) % n
        encrypted_message.append(encrypted_char)
    return encrypted_message

def decrypt_rsa(encrypted_message, n, d):
    # Decrypt the message
    decrypted_message = ''
    for encrypted_char in encrypted_message:
        # Decrypt using RSA
        decrypted_char = chr((encrypted_char ** d) % n)
        decrypted_message += decrypted_char
    return decrypted_message

# RSA parameters
n = 323  # Public modulus
e = 5    # Public exponent
d = 173  # Private exponent

# Original message
original_message = "Cryptographic Protocols"

# Encrypt the message
ciphertext = encrypt_rsa(original_message, n, e)

# Decrypt the ciphertext
decrypted_message = decrypt_rsa(ciphertext, n, d)

# Output results
print("Ciphertext (encrypted message):", ciphertext)
print("Decrypted message (should match original):", decrypted_message)
