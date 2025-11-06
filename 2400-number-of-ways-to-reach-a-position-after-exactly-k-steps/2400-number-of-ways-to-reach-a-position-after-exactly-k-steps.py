'''

In: start:int, end:int, k: int

Out: int -> num different ways we can reach end from start in k steps

1, 3, k=4

1, 2, 3, 4, 3
1, 0, 1, 2, 3


Principle: Break into smaller parts -> Solve subproblems -> Use the solutions to compose the larger solution. States can repeat -> Cache
    - Proof by induction: Solving f(start=1, k=3) = f(start=2, k=2) + f(start=0, k=2)

Two choices per number -> 2 ** K
- States repeat -> Cache


Time: O(2 ** N) w/o Memoization
Time: O(N ** 2) w/ Memoization

Space: O(K * N)

'''




class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        @cache
        def dp(i, k):

            if k == 0:
                if i == endPos:
                    return 1
                else:
                    return 0

            return dp(i + 1, k - 1) + dp(i - 1, k - 1)

        return dp(startPos, k) % (10**9 + 7)
        