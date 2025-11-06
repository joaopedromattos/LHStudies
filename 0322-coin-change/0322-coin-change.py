'''
In: List[int], amount: int
Out: int -> Fewest num of coins to a certain amount

Test 1
[1, 5, 10], amount = 12

5, 5, 1,1 -> 4 coins
10, 1, 1 -> 3 coins (good)

Test 2
[2, 5, 10], amount = 

5, 2, 2 -> 9, Return -1

Q: Are the coins sorted?

Principle: For every action, two decisions (pick the coin or not pick the coin), then the optimal of the ones that follow. (We can cache results because of this)

Algo:

For coin i:

1. Pick the coin
    (decrease the amount we have to match)

2. Stop picking the coin

Time complexity: O(2**coins), Space O(1)

W. Memoization

O(Coins ** 2), Space: O(Coins * Amount)

'''

from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(cur_coin, amnt):
            # This subproblem has ended, no coins left to try
            if cur_coin >= len(coins):
                if amnt == 0:
                    return 0
                else:
                    return inf

            # This "subproblem" has ended. No coins needed.
            if amnt == 0:
                return 0

            picked_coin = inf
            if amnt >= coins[cur_coin]:
                picked_coin = dp(cur_coin, amnt - coins[cur_coin]) + 1
            
            did_not_pick_coin = dp(cur_coin + 1, amnt)

            return min(picked_coin, did_not_pick_coin)

        min_coins = dp(0, amount)
        if min_coins == inf:
            return -1
        else:
            return min_coins
        