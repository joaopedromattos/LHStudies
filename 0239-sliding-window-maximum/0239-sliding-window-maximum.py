'''

arr = [-1, 2, -3, 4] k=2
max sliding window -> [2, 2, 4]

[(-1, 2), -3, 4] -> 2, max_idx = 1, new_idx = -1
[-1, (2, -3), 4] -> 2, max_idx = 1, new_idx = 2, nums[new_idx] > nums_max_idx ? 
[-1, 2,( -3, 4)] -> 4

Time O(n * k) -> Space O(1) or O(n)


--- 
Edge cases:
nums = [] k: 2 -> returns []
nums = [1] k: 1 -> [1]

'''
# Solution 1
# O(n * k) -> Terrible average case, because K can be very close to N
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slidingWindow = []
        for i in range(0, len(nums) - k + 1):
            slidingWindow.append(max(nums[i: i + k]))

        return slidingWindow


# Solution 2
# This is better, but the average case is still O(n * k)
# And this happens a lot, especially if K is large, this is a problem.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        def compute_max_in_window(window):
            max_idx = window.index(max(window))
            return max_idx
        
        
        max_idx = compute_max_in_window(nums[0:k])
        max_value = nums[max_idx]
        sliding_window = [max_value]
        for i in range(1, len(nums) - k + 1):
            if max_idx < i:
                max_idx = compute_max_in_window(nums[i:i + k])
                max_idx += i # Considering from where we started to count
                max_value = nums[max_idx]
                # print("Stale max value - recomputed : ", max_idx, i, max_value, 'window - ', nums[i:i + k])
            else:
                # Check if the new element
                # if larger than the previous max value
                most_recent_element = nums[i + k - 1]
                # print("Max value valid - comparing : ", max_idx, max_value, 'vs.',  most_recent_element)
                if most_recent_element > max_value:
                    max_value = most_recent_element
                    max_idx = i + k - 1

            sliding_window.append(max_value)
        return sliding_window


# Solution 3 (ideal)
# O(n) -> Every number enters the deque once, and is popped once
# This solution is somewhat similar to "Buying stocks" problem,
# but in a window.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []

        for i in range(len(nums)):
            

            # Case 1: Stale indexes:
            # If an index is smaller than 
            while d and d[0] <= i - k:
                d.popleft()

            # Case 2: Min from deque is smaller
            # than current num[i]. So essentially,
            # at every step we have to maintain *only*
            # the numbers that are larger than the current one
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            
            # Add current index, because it might
            # be the max of current window
            d.append(i)

            # as soon as the deque is populated
            if i >= k - 1:
                # The maximum of every window will always
                # be in the beginning of the deque
                max_idx = d[0]
                res.append(nums[max_idx])

        return res
        