class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0] * 3
        for i in nums:
            counts[i] += 1

        cur = 0
        for i in range(len(nums)):
            while counts[cur] == 0:
                cur += 1
            
            nums[i] = cur
            counts[cur] -= 1

        