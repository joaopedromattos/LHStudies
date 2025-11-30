''' 
In: int, int
Out: int

S _ _ _
_ p _ _
_ _ _ x

Principle: (by Induction) The number of unique paths starting from a postion i, j is the sum of the number of unique ways starting from (i, j + 1) (right) and starting from (i + 1, j) (down), i.e., independent of how we reached (i, j)


Time : O(2 ** (N * M)) -> Brute force vs. Memoization (M * N) (m and n are given)
Space : O(M + N) -> O(M * N)
'''

from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        
        @cache
        def dp(i, j):

            # Base case
            if (i == m - 1) and (j == n - 1):
                return 1
            
            num_paths_down = 0
            if i + 1 < m:
                num_paths_down += dp(i + 1, j)
            
            num_paths_right = 0
            if j + 1 < n:
                num_paths_right += dp(i, j + 1)

            return num_paths_down + num_paths_right


        return dp(0, 0)
            
        