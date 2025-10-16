'''
Input-> List[int] -> 2 * n
output -> int -> sum(list[(int, int)])


Tests: 
[1000, 1001, 1, 2] -> min(1, 2) + min(1000, 1001) -> 1001
- Main principle : The maximum sum is the one that minimizes the differences between each pair summed
    - Large numbers paired with large numbers
    - small numbers paired with small numbers

[inf, 2, -inf, 1] -> min(1, -inf), min(inf, 2) -> 3


Algo: 
Sort array -> sum pairs




'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        s = 0
        for i in range(0, len(nums) - 1, 2):
            s += min(new_nums[i], new_nums[i + 1])

        return s
        