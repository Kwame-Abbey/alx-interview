#!/usr/bin/python3
"""Defines a make change algorithm"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    Args:
        coins (list): Number of coins available
        total (int): Total amount
    Returns:
        Minimun number of coins or -1
    """
    # Check to see if total amount is zero
    if total <= 0:
        return 0

    minimum_coins = 0
    current_total = 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)

    # Looping through each coin in sorted(descending) list of coins
    for coin in coins:
        total_coin_used = (total - current_total) // coin
        current_total += total_coin_used * coin
        minimum_coins += total_coin_used

        if current_total == total:
            return minimum_coins

    return -1
