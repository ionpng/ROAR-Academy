import hashlib

def hash_password(password, salt=''):
    # Example using SHA-256
    return hashlib.sha256((salt + password).encode()).hexdigest()

def brute_force_attack(hash_to_crack, salt='', max_length=4):
    import itertools
    import string
    
    characters = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            if hash_password(password, salt) == hash_to_crack:
                return password
    return None

# Example usage
hashed_password = hash_password('password123')
print(f'Cracked password: {brute_force_attack(hashed_password)}')
