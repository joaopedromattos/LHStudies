'''
In: nums = List[int], target = int, Out: List[Int]

- Can we expect unique solution?
    - Follow up: are the numbers unique?
- Can we expect negative numbers?
- Can I consider we can store values in an Int?
- Can I assume the solution always exist or should we treat it?

[10, 1, 2, 5, 6], target = X

First idea: For every number, check all numbers (Trivial)

=> Has to be two numbers! We can store one of them in a data structure.

Principle: For a given idx j, we can look for the complementary num[j] = X - nums[i]. => store all nums[i] we have seen.

Time:O(n), Space: O(unique(nums))


'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}

        for idx, num in enumerate(nums):
            if target - num in num_to_idx:
                return [num_to_idx[target-num], idx]
            else:
                num_to_idx[num] = idx

        return -1
        