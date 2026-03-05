'''
In: List[List[Int]], Output: Int

- If I go from {1} => {1} is the effort 0 or 1?
    - Zero

Principle: For a given state (pos, effort_gain) -> the solution will only be optimal if all N positions and efforts (min (pos_i, effort_gain_i))
    - Memoization does not make sense because effort_gain is not a "pure" argument (depends on the previous state)

    Breadth first search => of all the paths, the "shortest" => lowest effort gain
        - but we have weights, so Dijkstra


Worst path to take: 

[c, c, c, c, c, ..., 1000]
[c, c+small, c+small+small...1000 ]

'''


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def isValid(pos):
            i, j = pos
            is_within_bounds = (0 <= i < len(heights) and 0 <= j < len(heights[0]))
            return is_within_bounds
        
        START_POINT = (0, 0)
        DESTINATION = (len(heights) - 1, len(heights[0]) - 1)
        movements = [(-1,0), (1,0), (0, 1), (0, -1)]

        min_effort_gain = {}
        min_effort_gain[START_POINT] = 0
        explore = [(0, START_POINT)]

        while explore:
            cur_max_effort, cur_pos = heapq.heappop(explore)

            i, j = cur_pos

            cur_height = heights[i][j]

            # Check if this is stale, because another
            # path has already updated this entry!
            if cur_max_effort != min_effort_gain[cur_pos]:
                continue

            for di, dj in movements:
                new_pos = (i + di, j + dj)
                new_i, new_j = new_pos
                
                if isValid(new_pos):
                    new_height = heights[new_i][new_j]

                    cand = max(cur_max_effort, abs(cur_height - new_height))

                    if cand < min_effort_gain.get(new_pos, math.inf):
                        min_effort_gain[new_pos] = cand
                        heapq.heappush(explore, (cand, new_pos))

        print(min_effort_gain)
        return min_effort_gain[DESTINATION]
                

# [1,2,3],
# [3,8,4],
# [5,3,5]
