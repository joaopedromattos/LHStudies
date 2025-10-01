# [1, 3, 4, 5, 6] [2, 3, 4, 7] -> [3, 4] -> 3
# O(N + M + logN) -> O(N)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1).intersection(set(nums2))
        nums = list(intersection)
        if nums == []:
            return -1
            
        return list(sorted(nums))[0]