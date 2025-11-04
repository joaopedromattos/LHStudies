'''

In: List[List[int]] -> m x n grid, m != n
Out: int

Main principle / demonstration: 
From any given point in the grid, the cost minimum cost does not depend on how you arrived there.
Ex.: from (1, 0) the minimum cost = 201 + how much it costed to arrive there (1).
    from (0, 1) the minimum cost is 103 + how much it costed to arrive there (1)

  1 100 1
  1 101 1


Complexity: 
Time -> For every position, 2 choices. -> M x N choices => O(2 ** (MxN))
Space -> There will be a total of 2 ** NxM function calls / allocations, but only O(NxM) calls will be allocated at the same time

With DP:
Time -> O(NxM)
Space -> O(NxM)

'''
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        
        m = len(grid)
        n = len(grid[0])

        @cache
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return grid[m - 1][n - 1]

            down_cost = inf
            if i + 1 < m:
                down_cost = dp(i + 1, j)

            right_cost = inf
            if j + 1 < n:
                right_cost = dp(i, j + 1)

            return min(down_cost, right_cost) + grid[i][j]

        return dp(0, 0)