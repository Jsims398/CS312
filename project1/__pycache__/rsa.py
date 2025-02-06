import random
import sys

# This may come in handy...
from fermat import miller_rabin

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
def ext_euclid(a: int, b: int) -> tuple[int, int, int]: #This function has a complexity of O(n^3) due to the recursive call O(n) and the mod operation O(n^2)
    if a < b: #C
        tmp = a #C
        a = b #C
        b = tmp #C

    if b == 0: #C
        return 1, 0, a #C
    x, y, d = ext_euclid(b, a % b) #n
    return y, x - (a // b)*y, d #n^2

# Implement this function
def generate_large_prime(bits=512) -> int: # We know that this function with n^4 complexity due to the miller_rabin function
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    ran_numb = random.getrandbits(bits) 
    while miller_rabin(ran_numb, 100) != "prime":
        ran_numb = random.getrandbits(bits)
    return ran_numb 


def euclid(a: int, b: int) -> int: #Has the complexity of O(n^3) due to the recursive call O(n) and the mod operation O(n^2)
    if b == 0:
        return a
    return euclid(b, a % b)

def relativePrime(n: int) -> int: #This function has a complexity of O(n^3) due to the euclid function
    for prime in primes:
        if euclid(prime, n) == 1:
            return prime
    return -1

# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]: #This function has a complexity of O(n^4) due to the generate_large_prime function
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    N = p * q
    e = relativePrime((p-1) * (q-1))
    while e == -1 or p == q:
        p = generate_large_prime(bits)
        q = generate_large_prime(bits)
        e = relativePrime((p-1) * (q-1))

    d = ext_euclid(e,(p-1)*(q-1))[1]
    d = d % ((p-1) * (q-1))
    return N, e, d