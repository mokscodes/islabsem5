// MD5,SHA-1, and SHA-256 
import time
import random
import string
import hashlib

# Function to generate random strings
def generate_random_strings(num_strings, length):
    return [''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(num_strings)]

# Hashing functions
def md5_hash(s):
    return hashlib.md5(s.encode()).hexdigest()  # Directly use hexdigest for cleaner output

def sha1_hash(s):
    return hashlib.sha1(s.encode()).hexdigest()

def sha256_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

# Collision detection
def detect_collisions(hashes):
    seen = set()
    collisions = set()
    for h in hashes:
        if h in seen:
            collisions.add(h)
        else:
            seen.add(h)
    return collisions

# Experiment
def experiment(num_strings=100, string_length=10):
    random_strings = generate_random_strings(num_strings, string_length)

    # MD5
    start_time = time.time()
    md5_hashes = [md5_hash(s) for s in random_strings]
    md5_time = time.time() - start_time
    md5_collisions = detect_collisions(md5_hashes)

    # SHA-1
    start_time = time.time()
    sha1_hashes = [sha1_hash(s) for s in random_strings]
    sha1_time = time.time() - start_time
    sha1_collisions = detect_collisions(sha1_hashes)

    # SHA-256
    start_time = time.time()
    sha256_hashes = [sha256_hash(s) for s in random_strings]
    sha256_time = time.time() - start_time
    sha256_collisions = detect_collisions(sha256_hashes)

    return {
        'MD5': {'time': md5_time, 'collisions': len(md5_collisions)},
        'SHA-1': {'time': sha1_time, 'collisions': len(sha1_collisions)},
        'SHA-256': {'time': sha256_time, 'collisions': len(sha256_collisions)},
    }

# Run the experiment
results = experiment()
print(results)
