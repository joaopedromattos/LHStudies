'''


In: List[List[int]], Output: int

-> What's the avg size of the matrix
-> Cells are 8-directionally connected but can we move to all 8 directions?
    - We are going to assume yes.
-> Is (0,0) always valid?


Principle: IF there is a path => We should return the shortest.
            ELSE:
                we have to be able to verify that (return -1)

-> Breadth-first search


'''


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] != 0:
            return -1


        # Checks if a movement is valid
        def isValid(pos):
            # We cannot stay where we are.
            if pos == (0, 0):
                return False

            # if it out of bounds
            within_bounds = (0 <= pos[0] < len(grid) and 0 <=pos[1] < len(grid[0]))
            is_zero = False
            if within_bounds:
                is_zero = grid[pos[0]][pos[1]] != 1

            return within_bounds and is_zero

        destination = (len(grid) - 1, len(grid[0]) - 1)

        dist = {(0, 0): 0}
        visited = set((0, 0))
        explore = deque([((0, 0), dist[(0, 0)])])

        possible_i = [-1, 0, 1]
        possible_j = [-1, 0, 1]

        while explore:
            cur_pos, cur_dist = explore.popleft()
            i, j = cur_pos

            for di in possible_i:
                for dj in possible_j:
                    new_pos = (i + di, j + dj)

                    if isValid(new_pos):
                        if new_pos in visited:
                            if cur_dist + 1 < dist[new_pos]:
                                dist[new_pos] = cur_dist + 1
                                explore.append((new_pos, dist[new_pos]))
                        else:
                            # visit
                            visited.add(new_pos)
                            dist[new_pos] = cur_dist + 1
                            explore.append((new_pos, dist[new_pos]))
        
        if destination in dist:
            return dist[destination] + 1
        else:
            return -1

                    
        