import random
import sys

# This may come in handy...
from fermat import *

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
# Here we raise the limit so the tests can run without any issue.
# Can you implement `mod_exp` and extended-euclid without recursion?
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Implement this function
def ext_euclid(a: int, b: int) -> tuple[int, int, int]: 
    if a < b:
        tmp = a
        a = b
        b = tmp 

    if b == 0: 
        return 1, 0, a 
    x, y, d = ext_euclid(b, a % b) 
    return y, x - (a // b)*y, d 

# Implement this function
def generate_large_prime(bits=512) -> int: # We know that this function with n^4 complexity due to the miller_rabin function
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    ran_numb = random.getrandbits(bits) 
    while fermat(ran_numb, 100) != "prime":
        ran_numb = random.getrandbits(bits)
    return ran_numb 

def get_e(phi: int) -> int:
    i = 0
    while i < len(primes):
        prime = primes[i]
        if ext_euclid(prime, phi)[2] == 1:
            return prime
        i += 1
    raise ValueError("No suitable prime found")

# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]: #This function has a complexity of O(n^4) due to the generate_large_prime function
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)
    N = p * q
    i = (p - 1) * (q - 1)
    
    e = get_e(i)

    d = ext_euclid(e, i)[1]
    if d < 0:
        d += i
    return N, e, d