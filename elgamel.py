# ElGamal Encryption
def elgamal_encrypt(p, g, h, message):
    import random

    k = random.randint(1, p-2)  # Random integer k
    c1 = pow(g, k, p)  # c1 = g^k mod p
    c2 = (h * pow(k, 1, p)) % p  # c2 = h^k * m mod p
    return c1, c2

# ElGamal Decryption
def elgamal_decrypt(p, x, c1, c2):
    s = pow(c1, x, p)  # s = c1^x mod p
    s_inv = pow(s, p-2, p)  # s_inv = s^(p-2) mod p (using Fermat's Little Theorem)
    m = (c2 * s_inv) % p  # m = c2 * s_inv mod p
    return m

# Parameters
p = 7919
g = 2
h = 6465
x = 2999
message = "Asymmetric Algorithms"

# Encrypt the message
c1, c2 = elgamal_encrypt(p, g, h, message)

# Decrypt the ciphertext
decrypted_message = elgamal_decrypt(p, x, c1, c2)

# Output
print("Ciphertext:", (c1, c2))
print("Decrypted message:", decrypted_message)
