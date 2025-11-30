'''
In: int (num people), dislikes (List[int, int])
Out: bool (whether it is a bipartite graph or not)


Test:

people: 5
"dislikes" / edges = [[1, 2], [3, 4], [3, 1] [0, 2], [4, 0]]

person = 0, [0], [2, 4], explore = [2, 4]
person = 2, [0, 1], [2, 4], explore = [4, 1]
person = 4, [0, 1], [2, 4], explore = [1, 3]
person = 1, [0, 1, 3], [2, 4], explore = [3]
person = 3, [0, 1, 3], [2, 4], explore = []

Principle: (By Induction) For a given node i, add neighbors to the other partition if they are not already there. If they are the same partition as i, then return False. This will be true for the i + 1 as well. Q.e.d.


O(V + E) (V number of peoeple, E number of dislikes)
O(V + E)


'''
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        G = [[] for i in range(n + 1)]
        for u, v in dislikes:
            G[u].append(v)
            G[v].append(u)

        # vis = [False] * (n + 1)
        # def components_starts(G, cur):
        #     nonlocal vis
        #     vis[cur] = True
        #     for neigh in G[cur]:
        #         if not vis[neigh]:
        #             components_starts(G, neigh)

        # starts = []
        # for i in range(1, n + 1):
        #     if not vis[i]:
        #         starts.append((i, 0))
        #         components_starts(G, i)


        # BFS
        vis = set()
        explore = deque([(1, 0)])
        partition = {0:set(), 1:set()}

        def opposite_partition(partition_value):
            if partition_value == 1:
                return 0
            else:
                return 1

        
        while explore or len(vis) < n:

            if len(explore) == 0:
                for i in range(1, n + 1):
                    if i not in vis:
                        explore.append((i, 0))
                        break

            cur_node, cur_partition = explore.popleft()
            vis.add(cur_node)

            for neighbor in G[cur_node]:
                if neighbor in partition[cur_partition]:
                    return False # Partitions should alternate

                neigh_partition = opposite_partition(cur_partition)
                partition[neigh_partition].add(neighbor)

                if not neighbor in vis:
                    explore.append((neighbor, neigh_partition))

        return True