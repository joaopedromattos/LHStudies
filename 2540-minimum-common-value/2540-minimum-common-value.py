# [1, 3, 4, 5, 6] [2, 3, 4, 7] -> [3, 4] -> 3
# O(N + M + logN) -> O(N)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]

            if nums1[i] < nums2[j]:
                i+=1
                continue
            
            if nums2[j] < nums1[i]:
                j+=1
                continue

        return -1