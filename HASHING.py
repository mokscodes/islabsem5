// HASHING
def hash_function(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash_value * 33 + ASCII
    return hash_value & 0xFFFFFFFF  # Ensure 32-bit range

# Example usage
result = hash_function("example")
print(result)
