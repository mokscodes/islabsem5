def additive_cipher_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Shift character and wrap around using modulo
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_message += encrypted_char
    return encrypted_message


def additive_cipher_decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            # Reverse the shift
            decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            decrypted_message += decrypted_char
    return decrypted_message


# Original message
message = "iamlearninginformationsecurity"
key = 20

# Encrypt the message
encrypted = additive_cipher_encrypt(message, key)
print("Encrypted Message:", encrypted)

# Decrypt the message
decrypted = additive_cipher_decrypt(encrypted, key)
print("Decrypted Message:", decrypted)
