'''
[-3, -2, 1, -1] -> [2, 1]

S => [0, -3, -1, 0, -1] -> [start, end) -> [_ , 3 or 0]

max S[i] and lowest S[j] s.t. j <= i

Time O(N) -> Space O(N)


[0, -2, -3]

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 2:
            return sum(nums)

        S = [0 for i in range(n + 1)]
        for i in range(1, n + 1): 
            S[i] = nums[i - 1] + S[i - 1]

        max_value, min_value = -inf, inf
        for i in range(n):
            min_value = min(S[i], min_value)

            max_value = max(max_value, S[i + 1] - min_value)

        return max_value
        