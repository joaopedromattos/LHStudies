# Solution 2: 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        
        for n in nums:
            # If our current sum is negative,
            # We can just ignore this prefix
            if cur_sum < 0:
                cur_sum = 0
                
            cur_sum += n # We are gonna take the current element and face the consequences
            max_sum = max(max_sum, cur_sum)
        return max_sum
        