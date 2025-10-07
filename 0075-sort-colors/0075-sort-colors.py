'''

# Solution 1
num_red, num_white, num_blue = 0,0,0 -> Counters

[2, 1, 0,] -scan through array-> [0 , 0, 1, 1, 2, 2]

# Solution 2
l, m, h = 0, 0, len(nums) - 1 l--reds---m--whites-h-blues-|

high < mid ? -> swap
low > mid ? -> swap
mid walks
low walks

[2, 2, 1,] -> 
l   m  h

[1, 2, 0,] -> mid > high, swap
l   m  h          

[0, 1, 2] -> mid > high, swap
l   m  h          

    blue    red     white
l   sp H    moves   sp M
m   sp H    sp L    moves    
h   moves   sp L    sp M

Time O(N) -> Space O(1)

'''

class Solution:
    

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, h = 0, 0, len(nums)-1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:  # nums[m] == 2
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
