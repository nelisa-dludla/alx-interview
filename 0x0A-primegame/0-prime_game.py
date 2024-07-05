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
        'Maria': {
                'overallWins': 0,
                'roundWins': 0,
                'roundMoves': 0,
            },
        'Ben': {
                'overallWins': 0,
                'roundWins': 0,
                'roundMoves': 0,
           }
    }

    # Rounds
    for n in nums:
        current_array = list(range(1, n + 1))
        current_player = 'Maria'
        moves = 0

        while any(isPrime(num) for num in current_array):
            # Find smallest prime number in current_array
            for num in current_array:
                if isPrime(num):
                    current_array = findMul(num, current_array)
                    moves += 1
                    break

                # Switch players
                if current_player == 'Maria':
                    current_player = 'Ben'
                else:
                    current_player = 'Maria'

        # Determine winner of the round
        if moves % 2 == 1:
            winner = 'Maria'
        else:
            winner = 'Ben'

            playerStats[winner]['overallWins'] += 1

    # Determine overall winner
    if playerStats['Maria']['overallWins'] > playerStats['Ben']['overallWins']:
        return 'Maria'
    elif playerStats['Ben']['overallWins'] > playerStats['Maria']['overallWins']:
        return 'Ben'
    else:
        return None
