# 1. Find the closest number to x, k times, always removing the current element.
# Time: O(klogn) -> Space O(k) or O(n + k)
# "Adversarial case" -> [1 1 1 2 4 5] -> k=2, x=3 -> Ans: [2, 4]

import bisect 

class Solution:


    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binary_search(arr, x):
            low = -1
            high = len(arr)

            while high - low > 1:
                mid = (high + low) // 2

                if arr[mid] < x:
                    low = mid
                else:
                    high = mid
            
            # In case our x is the last or first of the list
            low, high = max(low, 0), min(high, len(arr) - 1)

            if abs(arr[low] - x) <= abs(arr[high] - x):
                return low, arr[low]
            else:
                return high, arr[high]

        if len(arr) <= k:
            return arr


        k_closest_elemen = []

        for i in range(k):
            idx, val = binary_search(arr, x)
            bisect.insort(k_closest_elemen, val)
            arr.pop(idx)

        return k_closest_elemen
        