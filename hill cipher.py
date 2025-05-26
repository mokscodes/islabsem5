import numpy as np

def prepare_message(message):
    # Remove spaces and convert to lowercase
    message = message.replace(" ", "").lower()
    return message

def create_key_matrix(key):
    # Create a 2x2 key matrix
    return np.array(key).reshape(2, 2)

def encrypt_hill_cipher(message, key):
    # Prepare the message
    message = prepare_message(message)
    
    # Create the key matrix
    key_matrix = create_key_matrix(key)
    
    # Prepare the message into pairs
    message_pairs = []
    for i in range(0, len(message), 2):
        if i + 1 < len(message):
            message_pairs.append([ord(message[i]) - ord('a'), ord(message[i + 1]) - ord('a')])
        else:
            message_pairs.append([ord(message[i]) - ord('a'), 0])  # Padding with 'a' if odd length
    
    # Encrypt the message
    encrypted_message = ""
    for pair in message_pairs:
        encrypted_vector = np.dot(key_matrix, pair) % 26
        encrypted_message += chr(encrypted_vector[0] + ord('a')) + chr(encrypted_vector[1] + ord('a'))
    
    return encrypted_message

# Original message
message = "We live in an insecure world"
key = [3, 3, 2, 7]

# Encrypt the message
encrypted = encrypt_hill_cipher(message, key)
print("Encrypted Message (Hill Cipher):", encrypted)
