#!/usr/bin/python3
''' Solution to interview question prime game
'''


def isWinner(x, nums):
    '''Returns overall winner of prime game
    '''
    def isPrime(num):
        '''Return "True" if num is a prime number
        '''
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    def findMul(num, array):
        '''Find multiples and remove them from array
        '''
        return [x for x in array if x % num != 0]

    # Players
    playerStats = {
        'Maria': 0,
        'Ben': 0
    }

    # Rounds
    for n in nums:
        current_array = list(range(1, n + 1))
        current_player = 'Maria'

        while any(isPrime(num) for num in current_array):
            # Find smallest prime number in current_array
            for num in current_array:
                if isPrime(num):
                    current_array = findMul(num, current_array)
                    break

                # Switch players
                if current_player == 'Maria':
                    current_player = 'Ben'
                else:
                    current_player = 'Maria'

        # Determine winner of the round
        if current_player == 'Maria':
            winner = 'Ben'
        else:
            winner = 'Maria'

        playerStats[winner] += 1

    # Determine overall winner
    if playerStats['Maria'] > playerStats['Ben']:
        return 'Maria'
    elif playerStats['Ben'] > playerStats['Maria']:
        return 'Ben'
    else:
        return None
