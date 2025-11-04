'''

ins : List[int] Outs: int (min number of jumps)

Ex:

[2, n, 1, 1, 1, 1] -> beeing greedy in the beginning, does not payoff

[3, 1, 3, 1, 1, 1] -> More than one position yields the best result.


Principle: 
- What happened before I reached my current position, will not change the optimal value of my position.


Algo: 
f(0) -> min([f(0 + i) for i in range(f(0))])

Time: O(N**(N-1) ) -> No cache -> O(N**2) (With cache)
Space: O(1) -> No-> No cache -> O(N)


'''
from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            if i == len(nums) - 1:
                return 0
            
            min_this_step = inf
            for skips in range(1, nums[i] + 1):
                next_position = min(i + skips, len(nums) - 1)
                min_this_step = min(min_this_step, dp(next_position))

            return min_this_step + 1

        return dp(0)
        