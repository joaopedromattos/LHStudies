'''
In: n = int
Out: int -> max product from numbers before n

n = 7
1, 6 -> 6
3, 3, 1 ->9
3, 4 -> 12
5, 2 -> 10
...


F(n = 7)
prod([1, F(7 - 1)]) -> prod([1, F(6 - 1)])
prod([2, F(7 - 2)])
prod([3, F(7 - 3)])
...
prod([6, F(7 - 6)])

Principle: Product between the "current number", and the subproblem corresponding to the remaining number.

Algo:
    i in 1...number - 1
        max(prod([i, dp(number - i)]))

Time O(N ** N) -> w/ Memoization O(N ** 2)
Space O(1) -> W/ Memoization O(N ** 2)

'''


from math import prod
class Solution:
    def integerBreak(self, n: int) -> int:

        @cache
        def dp(number):
            if number == 0:
                return 0

            if number == 1:
                return 1

            max_product = 0
            for i in range(1, number):
                max_product = max(max_product, i * (number - i), prod([i, dp(number - i)]))

            return max_product
            
        return dp(n)