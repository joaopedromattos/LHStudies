'''

k minutes => k is small not all oranges will be rotten. K is large (enough) then all the oranges will always be rotten before K.

|00000000011111111111111111111......
0         k 

Principle: 1 - Search the minimum -> Binary search problem
            2 - Evaluate (for a fixed given k ) whether there's a scenario in which all oranges get rotten. (BFS)


O(log n * (grid) ** 2)
'''


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))

    
        g = copy.deepcopy(grid)
        vis = [[ False for j in range(len(grid[0]))] for i in range(len(grid))]
        explore = deque([(0, rotten_fruit) for rotten_fruit in rotten])
        timestamp = 0
        print(explore)
        fresh_oranges = False
        while explore:

            timestamp, (i, j) = explore.popleft()
            vis[i][j] = True

            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_i = (i + di)
                new_j = (j + dj)

                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue

                if not vis[new_i][new_j] and g[new_i][new_j] == 1:
                    print(i, j, "Contaminates", new_i, new_j, 'timestamp:', timestamp + 1, 'explore', explore)
                    explore.append((timestamp + 1, (new_i, new_j)))
                    g[new_i][new_j] = 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if g[i][j] == 1:
                    return -1
                    
        return timestamp

        

        