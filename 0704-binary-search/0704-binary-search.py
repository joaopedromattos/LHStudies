# [-1, 9, 30, 40], target = 10
#  0.  0    1.  1
# C[k] := arr[k] > target




class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1


        l = -1
        h = len(nums)

        while h - l > 1: # pointers are not consective
            mid = (l + h) // 2

            if nums[mid] > target:
                h = mid
            else:
                l = mid

            
        if nums[l] == target:
            return l
        else:
            return -1
        