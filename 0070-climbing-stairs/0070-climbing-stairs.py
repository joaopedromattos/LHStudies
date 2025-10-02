'''
n = 4

R:4 1 -> R: 3 (1 or 2) -> R: 2 (1 or 2) <Reuse> 

R:4 2 -> R: 2 (1 or 2) 

Time O(2^n) -> O(N)
Space O(1) -> O(N)
'''

class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache
        def dp(remaining: int):

            if remaining == 0:
                return 1

            if remaining < 0:
                return 0

            return dp(remaining - 1) + dp(remaining - 2)

        return dp(remaining=n)

            
        