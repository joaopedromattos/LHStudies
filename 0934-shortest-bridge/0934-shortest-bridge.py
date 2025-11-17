'''
In: List[List[int]]
Output: int

Test
1 1 0 
1 0 1
0 1 1


Out: 1 -> Three possibilities.


Principle: If we are going to a position that is a 1, then we are inside the island -> no cost / no bridge.
            if we are going to a position that is 0, then we have to flip.
            for any (i, j), we want the minimum cost, considering that the price of every movement is the same





Time: O(n ** 2)
Space = O(N ** 2) (If considering the input as well)


'''

from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # Find one 1 to start
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and start is None:
                    start = (i, j)
        
        border = set()
        first_island = set()
        def dfs(i, j):
            nonlocal border
            
            first_island.add((i, j))

            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]

            for ii, jj in zip(di, dj):
                if 0 <= (i + ii) < len(grid) and 0 <= (j + jj) < len(grid) and (i + ii, j + jj) not in first_island:
                    if grid[i + ii][j + jj] != 1:
                        # we are in a border
                        border.add((i, j, 0))
                    else:
                        dfs(i + ii, j + jj)

            return
        
        dfs(start[0], start[1])

        vis = {(i, j) : v for (i, j, v) in border}

        explore = deque(border)

        second_island_border = set()
        while explore:
            i, j, cost = explore.popleft()

            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]

            for ii, jj in zip(di, dj):
                if 0 <= (i + ii) < len(grid) and 0 <= (j + jj) < len(grid):
                    
                    if (i + ii, j + jj) in vis:
                        continue

                    if (i + ii, j + jj) in first_island:
                        continue

                    if grid[i + ii][j + jj] == 1:
                        return cost

                    if (i + ii, j + jj) not in vis or cost + 1 < vis[(i + ii, j + jj)]:

                        vis[(i + ii, j + jj)] = cost + 1
                        explore.append((i + ii, j + jj, cost + 1))

        # In theory we should always connect, given problem constraints
        return -1
            


        

                    
        


        

        
        