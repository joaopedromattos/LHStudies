'''
In: List[List[int]], nodes (N), k=> start
out: List[int] -> [time_i, ....]


Test:

[[0, 1, 10], [1, 2, 1], [0, 2, 1000]]

[0] -> [1, 2] => [0, 10, 1000]
[1] -> [2, 2] => [0, 10, 11]
[2] -> [] (Finish)
[0, 10, 11]

Principle: Breadth-first search for the "cummulative minimum" -> min(Time it took to arrive to the next node before vs the time it takes to arrive to the next node from current node)

Time: O(V + E)
Space: O(V + E) => for every node, store all neighbors. So V lists of E elements combined.

'''

from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        n += 1
        G = [[] for i in range(n)]

        for u, v, time in times:
            G[u].append((v, time))


        min_dist = [inf] * n
        min_dist[k] = 0
        to_visit = deque([(k, 0)])

        while to_visit:
            
            cur_node, time = to_visit.popleft()

            for neigh, neigh_time in G[cur_node]:
                # If something is better than what I've found
                # I will (re)explore
                if neigh_time + time < min_dist[neigh]:
                    min_dist[neigh] = neigh_time + time
                    to_visit.append((neigh, min_dist[neigh]))

        max_value = max(min_dist[1:])
        return -1 if max_value == inf else max_value