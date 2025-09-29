# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# [1, 2, 3, 4] -> bad = 3
# O(log(n))
from math import ceil
class Solution:
    def firstBadVersion(self, n: int) -> int:

        if n == 0:
            return 0
        
        if n == 1:
            return 1

        low, high= 1, n
        while low < high:
            mid = (high + low) // 2
            response = isBadVersion(mid)
            if response:
                high = mid
            else:
                low = mid + 1 # avoids infinite loops

        return high


        