# Playfair Cipher implementation

# Remove duplicates while preserving order in the key
def remove_duplicates(word):
    result = []
    for char in word:
        if char not in result:
            result.append(char)
    return ''.join(result)

# Create a 5x5 Playfair matrix from the secret key
def create_playfair_matrix(secret_key):
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J are considered the same
    secret_key = remove_duplicates(secret_key.upper().replace("J", "I"))
    
    # Fill the matrix with the key first, then the remaining letters
    for char in secret_key:
        if char not in matrix:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    # Convert the list to a 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]

# Find the position of a letter in the Playfair matrix
def find_position(letter, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

# Encrypt a pair of letters using Playfair cipher
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    # Rule 1: Same row
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    # Rule 2: Same column
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    # Rule 3: Rectangle swap
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Process the plaintext to prepare for encryption
def prepare_plaintext(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    digraphs = []
    i = 0

    while i < len(plaintext):
        pair = plaintext[i]
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i + 1]:  # If letters are the same, insert 'X'
                pair += 'X'
            else:
                pair += plaintext[i + 1]
                i += 1
        else:
            pair += 'X'  # If single letter left at the end, append 'X'
        digraphs.append(pair)
        i += 1

    return digraphs

# Encrypt the plaintext message
def playfair_encrypt(plaintext, secret_key):
    matrix = create_playfair_matrix(secret_key)
    digraphs = prepare_plaintext(plaintext)
    ciphertext = ""

    for pair in digraphs:
        ciphertext += encrypt_pair(pair, matrix)

    return ciphertext

# Input
secret_key = "GUIDANCE"
plaintext_message = "The key is hidden under the door pad"

# Encrypt the message using Playfair cipher
ciphertext = playfair_encrypt(plaintext_message, secret_key)
print("Ciphertext:", ciphertext)
# Playfair Cipher implementation

# Remove duplicates while preserving order in the key
def remove_duplicates(word):
    result = []
    for char in word:
        if char not in result:
            result.append(char)
    return ''.join(result)

# Create a 5x5 Playfair matrix from the secret key
def create_playfair_matrix(secret_key):
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J are considered the same
    secret_key = remove_duplicates(secret_key.upper().replace("J", "I"))
    
    # Fill the matrix with the key first, then the remaining letters
    for char in secret_key:
        if char not in matrix:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    # Convert the list to a 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]

# Find the position of a letter in the Playfair matrix
def find_position(letter, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

# Encrypt a pair of letters using Playfair cipher
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    # Rule 1: Same row
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    # Rule 2: Same column
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    # Rule 3: Rectangle swap
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Process the plaintext to prepare for encryption
def prepare_plaintext(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    digraphs = []
    i = 0

    while i < len(plaintext):
        pair = plaintext[i]
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i + 1]:  # If letters are the same, insert 'X'
                pair += 'X'
            else:
                pair += plaintext[i + 1]
                i += 1
        else:
            pair += 'X'  # If single letter left at the end, append 'X'
        digraphs.append(pair)
        i += 1

    return digraphs

# Encrypt the plaintext message
def playfair_encrypt(plaintext, secret_key):
    matrix = create_playfair_matrix(secret_key)
    digraphs = prepare_plaintext(plaintext)
    ciphertext = ""

    for pair in digraphs:
        ciphertext += encrypt_pair(pair, matrix)

    return ciphertext

# Input
secret_key = "GUIDANCE"
plaintext_message = "The key is hidden under the door pad"

# Encrypt the message using Playfair cipher
ciphertext = playfair_encrypt(plaintext_message, secret_key)
print("Ciphertext:",ciphertext)
