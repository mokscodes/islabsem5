def vigenere_cipher_encrypt(message, key):
    encrypted_message = ""
    key_length = len(key)
    key_index = 0

    for char in message:
        if char.isalpha():
            # Calculate the shift
            shift = ord(key[key_index % key_length]) - ord('a')
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_message += encrypted_char
            key_index += 1  # Move to the next character in the key
    return encrypted_message


def vigenere_cipher_decrypt(encrypted_message, key):
    decrypted_message = ""
    key_length = len(key)
    key_index = 0

    for char in encrypted_message:
        if char.isalpha():
            # Calculate the reverse shift
            shift = ord(key[key_index % key_length]) - ord('a')
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_message += decrypted_char
            key_index += 1  # Move to the next character in the key
    return decrypted_message


# Original message
message = "thehouseisbeingsoldtonight"
key = "dollars"

# Encrypt the message
encrypted = vigenere_cipher_encrypt(message, key)
print("Encrypted Message (Vigenère):", encrypted)

# Decrypt the message
decrypted = vigenere_cipher_decrypt(encrypted, key)
print("Decrypted Message (Vigenère):", decrypted)
