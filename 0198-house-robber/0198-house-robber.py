'''

In: arr = List[int]
Out: int -> maximum money

[100, 101, 4, 1] -> 104
[100, 4, 101, 1] -> 202


Principle: There are two choices per house (rob or not rob) -> Solving the subproblems <=> Solving the larger problem (Dinnamic Programming Algo)

Algo:
For house i: 
    if rob (reward arr[i]) 
        Go to the next-next house
    else:
        not rob (reward : 0)
        Go to next house


Time: O(2 ** n), Space: O(1) (Regardless of implementation)

With memoization:
Time: O(N ** 2), Space O(N) (Store the best solution for that house)
'''

from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        num_houses = len(nums)

        @cache
        def dp(cur_house):

            if cur_house >= num_houses: # no houses to steal
                return 0

            return max(dp(cur_house + 2) + nums[cur_house], dp(cur_house + 1))

        return dp(0)


            
        


        
        