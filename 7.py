import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return [p for p in range(2, limit + 1) if is_prime[p]]

# Function to find the n-th prime
def find_nth_prime(n):
    # Start with an initial estimate for the upper bound
    limit = int(n * (math.log(n) + math.log(math.log(n))))  # A better approximation
    primes = []
    
    while len(primes) < n:
        primes = sieve_of_eratosthenes(limit)
        limit *= 2  # Double the limit if not enough primes found

    return primes[n - 1]  # Return the n-th prime (0-indexed)

# Get the 10,001st prime
nth_prime = find_nth_prime(10001)
print(nth_prime)
