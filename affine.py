def affine_cipher_encrypt(message, a, b):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Apply the affine transformation
            encrypted_char = chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            encrypted_message += encrypted_char
    return encrypted_message


def affine_cipher_decrypt(encrypted_message, a, b):
    decrypted_message = ""
    # Find the modular multiplicative inverse of a
    inverse_a = pow(a, -1, 26)
    for char in encrypted_message:
        if char.isalpha():
            decrypted_char = chr((inverse_a * ((ord(char) - ord('a')) - b)) % 26 + ord('a'))
            decrypted_message += decrypted_char
    return decrypted_message


# Original message
message = "iamlearninginformationsecurity"
a = 15
b = 20

# Encrypt the message
encrypted = affine_cipher_encrypt(message, a, b)
print("Encrypted Message:", encrypted)

# Decrypt the message
decrypted = affine_cipher_decrypt(encrypted, a, b)
print("Decrypted Message:", decrypted)
