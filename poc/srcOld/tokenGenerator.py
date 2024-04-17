##
## Gaby, 2024
## poc
## File description:
## randomStr
##

import random
import string
import time

def randomStr(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def sha256(string):
    import hashlib
    return hashlib.sha256(string.encode()).hexdigest()

def main():
    seed = randomStr(16)
    hashed = sha256(seed)
    print("SHA256 hash of '%s': %s" % (seed, hashed))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Python execution time: %.6f seconds" % (time.time() - start_time))

