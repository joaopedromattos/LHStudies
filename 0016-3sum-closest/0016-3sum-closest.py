'''
[3, 4, 1, 2] -> target = 6

3 -> target = 6 - 3 = 3
4 -> target = 3 - 4 = -1
1 -> skip
2 -> skip
3 -> 4 -> x
----

3 -> target = 3
1 -> target = 2
2 -> target = 0
3 -> 1 -> 2 (OK)

4 -> target = 2
1 -> target = 1
2 -> skip
4 -> 1 -> x
----
Naive solution -> Time O(N!) -> "For every element, check every remaining element"

# Solution 2:
1. Sorting -> Enables using a second pointer. At every test, you will know if you are getting closer to 
2. Sum from the back and from the front of the array

Time -> O(N^2 + nlogn) (Search + Sorting)
Space -> O(1) (If you do not consider the input)
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, h = i + 1, len(nums) - 1
            
            while h - l > 0:

                total = nums[i] + nums[l] + nums[h]

                # If the current number is closer to 
                # the target than the previous one
                if abs(total - target) < abs(target - res):
                    res = total

                if total == target:
                    return total
                
                

                if total < target:
                    # our low, is too low
                    l += 1
                else:
                    # our high, is too high
                    h -= 1

        return res





        