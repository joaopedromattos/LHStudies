'''
In: arr: List[int]
Out: int -> max sum of circular subarray

[1, -1000, 2, 3] -> [2, 3] -> 5
[1, -1000, 2, -3] -> [2] -> 2
[1, -1000, 2, 0] -> [2, 0, 1] -> 3

Not circular version -> Prefix sum.
Circular -> Every element is the start of the prefix.

Principle: A subarray is an interval defined by start and end. Moving the start forward just subtracts position i. Moving end forward, just adds position i.

[..., W, [X, ....., Y], Z, ...] -> [..., W, [X, ....., Y, Z], ...] Is just the preivous state + Z
[..., W, [X, ....., Y], Z, ...] -> [..., W, X, [....., Y], Z, ...] Is just the preivous state - X

Algo:
- (i, j)
    
    call (i, j + 1) # adding one number


    
    call (i + 1, j) # deleting one number

Time -> Naive O(N**2) / O(N)
Space -> O(N) (Without considering the input)  / O(N ** 2)


'''

class Solution:

    # def maxSubarraySumCircular(self, nums: List[int]) -> int:

    #     n = len(nums)

    #     new_nums = CustomList(nums)

    #     @cache
    #     def dp(i, j)

    #         # Base cases:
    #         if i >= j:
    #             return 0

    #         if j-i == 1:
    #             return new_nums[i:j]

    #         sum_current_window = sum(new_nums[i:j])

    #         window_delete = dp((i + 1) % n, j % n)

    #         window_add = dp(i % n, (j + 1) % n)

    #         return max(sum_current_window, window_delete, window_add)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]

        # Prefix sums S where S[0] = 0 and S[i] = sum(nums[:i])
        S = [0] * (n + 1)
        for i in range(1, n + 1):
            S[i] = S[i - 1] + nums[i - 1]

        total = S[-1]

        # Best linear subarray via prefix sums: max(S[j+1] - min_prefix up to j)
        max_value, min_prefix = -inf, inf
        for i in range(n):
            min_prefix = min(min_prefix, S[i])
            max_value = max(max_value, S[i + 1] - min_prefix)

        # All-negative guard: if best linear < 0, wrapping would choose empty set -> invalid
        if max_value < 0:
            return max_value

        # Min subarray via prefix sums: min(S[j+1] - max_prefix up to j)
        min_sub, max_prefix = inf, -inf
        for i in range(n):
            max_prefix = max(max_prefix, S[i])
            min_sub = min(min_sub, S[i + 1] - max_prefix)

        # Wrap candidate = total - min_sub
        return max(max_value, total - min_sub)

        