#!/usr/bin/python3
"""Defines an algorithm for Prime game
"""


def isWinner(x, nums):
    """Main function"""
    def sieve(max_n):
        """Generate list of booleans representing primality
        of numbers 0 to max_n.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    def count_primes(is_prime):
        """Generate a list where index i contains the
        number of primes from 0 to i.
        """
        prime_count = [0] * len(is_prime)
        count = 0
        for i in range(len(is_prime)):
            if is_prime[i]:
                count += 1
            prime_count[i] = count
        return prime_count

    if not nums or x <= 0:
        return None

    max_n = max(nums)
    is_prime = sieve(max_n)
    prime_count = count_primes(is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
