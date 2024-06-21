#!/usr/bin/python3
'''Coin change problem
'''


def makeChange(coins, total):
    '''Solution to coin change problem
    '''
    if total <= 0:
        return 0

    max_coins = total + 1
    dp = [max_coins] * (total + 1)
    dp[0] = 0

    i = 0
    while i < len(coins):
        coin = coins[i]
        j = coin
        while j <= total:
            dp[j] = min(dp[j], dp[j - coin] + 1)
            j += 1
        i += 1

    if dp[total] == max_coins:
        return -1
    else:
        return dp[total]
