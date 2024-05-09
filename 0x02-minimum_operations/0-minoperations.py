#!/usr/bin/python3
"""Defines an algorithm for finding the
minimum operations required
"""


def prime_factorization(num):
    """Returns a list of all the prime factors of a number"""
    factors_list = list()
    divisor = 2
    while (divisor <= num):
        if (num % divisor) == 0:
            factors_list.append(divisor)
            num /= divisor
        else:
            divisor += 1
    return factors_list


def minOperations(n):
    """Returns the number of minimum operations required"""
    min = 0
    prime_facts = prime_factorization(n)
    nb_occurences = {fact: prime_facts.count(fact) for fact in prime_facts}
    for key, value in nb_occurences.items():
        min += key * value
    return min
