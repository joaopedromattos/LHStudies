'''

In : LIst[int]
Out: int -> Len of the longest subsequence of strictly increasing

Test
[10, 1, 2, 12, 13]  -> Solution 1:  10, 12, 13 Solution 2: 1, 2, 12, 13

Principle: Every number is the start of a sequence of length 1, and it calls for the next successor on the list.

Trivial solution: Time O(N**2) -> Starting at every number we check all positions.
                  Space O(1)

Smarter solutions: Every position that preceeds position i *might* pass by i. 
                    Because i might be someones succesor. So we re-use the result.


Following the example:
[10, 1, 2, 12, 13]:
f(0) -> 10 + f(3)
f(3) -> 12 + f(4)
f(4) -> 13


f(1) -> 1 + f(2)
f(2) -> 2 + f(3) <cache hit>
f(3) -> 12 + f(4) <cache hit>
f(4) -> 13


Time complexity: O(n "logn") -> N states -> at every pass the array keeps being more and more cached. -> Worst case: alternating sequences -> Half of the array is cached per pass. (log n)

Space: O(n)

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dp(i):
            print('calling to,', i)
            if i > len(nums):
                return 0
            
            local_max_length = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    local_max_length = max(local_max_length, dp(j) + 1)
            
            return max(local_max_length, 1)

        max_length = 0
        for i in range(len(nums)):
            print('starting at', i)
            max_length = max(max_length, dp(i))

        return max_length
        