'''
In: int, connections (edges)
Out: how many ops to make it connected vs how many edges we have


Principle: Components vs "spare edges" (edges that we did not use).

If we have three components, and 2 spare edges, we can connect the entire network.

If we have 6 components, 5 spare edges

If we have X, we need X - 1


DFS O(N + V)
Space : N + V
'''



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        G = [[] for i in range(n)]
        for u,v in connections: 
            G[u].append(v)
            G[v].append(u)

        visited = [False] * n
        edges_used = []
        def traverse(cur):
            nonlocal visited, edges_used
            visited[cur] = True
            for neigh in G[cur]:
                if not visited[neigh]:
                    edges_used.append((cur, neigh))
                    traverse(neigh)

        components = 0
        for i in range(n):
            if not visited[i]:
                traverse(i)
                components += 1

        

        num_edges_required = components - 1

        spare_edges = len(connections) - len(edges_used)

        if spare_edges >= num_edges_required:
            return num_edges_required
        else:
            return -1



        