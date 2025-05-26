def autokey_cipher_encrypt(plaintext, key):
    ciphertext = ""
    prev_val = key
    for char in plaintext:
        ascii_val = ord(char)
        encrypted_val = (ascii_val + prev_val) % 256
        ciphertext += chr(encrypted_val)
        prev_val = encrypted_val
    return ciphertext

def autokey_cipher_decrypt(ciphertext, key):
    plaintext = ""
    prev_val = key
    for char in ciphertext:
        ascii_val = ord(char)
        decrypted_val = (ascii_val - prev_val) % 256
        plaintext += chr(decrypted_val)
        prev_val = ascii_val
    return plaintext

plaintext = "thehouseisbeingsoldtonight"
key = 7

ciphertext = autokey_cipher_encrypt(plaintext, key)
print("Encrypted message:", ciphertext)

decrypted_text = autokey_cipher_decrypt(ciphertext, key)
print("Decrypted message:",decrypted_text)
