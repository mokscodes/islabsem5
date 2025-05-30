def multiplicative_cipher_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Shift character and wrap around using modulo
            encrypted_char = chr((ord(char) - ord('a')) * key % 26 + ord('a'))
            encrypted_message += encrypted_char
    return encrypted_message


def multiplicative_cipher_decrypt(encrypted_message, key):
    decrypted_message = ""
    # Find the modular multiplicative inverse of the key
    inverse_key = pow(key, -1, 26)
    for char in encrypted_message:
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord('a')) * inverse_key % 26 + ord('a'))
            decrypted_message += decrypted_char
    return decrypted_message


# Original message
message = "iamlearninginformationsecurity"
key = 15

# Encrypt the message
encrypted = multiplicative_cipher_encrypt(message, key)
print("Encrypted Message:", encrypted)

# Decrypt the message
decrypted = multiplicative_cipher_decrypt(encrypted, key)
print("Decrypted Message:", decrypted)
