'''
[1,4,3,2] -> sort() -> [1, 2, 3, 4] -> min(1, 2) + min(3, 4) => 4

Time O(nlogn) -> O(1) / O(n)
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        sorted_nums = list(sorted(nums))
        min_sum = 0
        for i in range(0, len(sorted_nums), 2):
            min_sum += min(sorted_nums[i], sorted_nums[i + 1])

        return min_sum