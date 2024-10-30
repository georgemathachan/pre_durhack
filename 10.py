import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime

def sum_of_primes(limit):
    is_prime = sieve_of_eratosthenes(limit)
    return sum(i for i, prime in enumerate(is_prime) if prime)

# Calculate the sum of primes below 2,000,001
total_sum = sum_of_primes(2000000)
print(total_sum)
