'''
[-3, -2, 1, -1] -> [2, 1]

S => [0, -3, -1, 0, -1] -> [start, end) -> [_ , 3 or 0]

max S[i] and lowest S[j] s.t. j <= i

Time O(N) -> Space O(N)


[0, -2, -3]

'''

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
        
#         n = len(nums)

#         if n < 2:
#             return sum(nums)

#         S = [0 for i in range(n + 1)]
#         for i in range(1, n + 1): 
#             S[i] = nums[i - 1] + S[i - 1]

#         max_value, min_value = -inf, inf
#         for i in range(n):
#             min_value = min(S[i], min_value)

#             max_value = max(max_value, S[i + 1] - min_value)

#         return max_value




'''
In: List[int]
Out: Int

[3, -1, 1, 4] -> [3, -1, 1, 4]
[3, -1000, 1, 4, -1000, 10_000] -> [1, 4] -> -1000 outsums everything that comes before


S => [0, 3, 2, 3, 7]
min_idx => 0
max_idx = 

Principle: 
Looking for where to start the array and where to end the array.
We will start the array when *the sum of what comes before is positive* <prefix>
We will end the array when *the sum of what comes before <becomes> negative* <first negative prefix>

Simple terms: What's the smallest number? What's the largest number that comes after the smallest number? 

Time O(N)
Space O(N)

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return sum(nums)

        S = [0 for i in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            S[i] = S[i - 1] + nums[i - 1]

        max_value, min_value = -inf, inf
        for i in range(len(nums)):
            min_value = min(min_value, S[i]) # things "only exist" after the smallest value.

            max_value = max(max_value, S[i + 1] - min_value)


        return max_value

        






        