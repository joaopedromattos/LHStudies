'''
[0, 1][2, 3][0, 2] -> Source 0 Dest 3
0 -> [1, 2]
1 -> x
2 -> [3]
3 -> True

len({0, 1, 2, 3}) == n -> False

Time O(E) -> Space O(E)
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # Creating our graph
        G = {i : [] for i in range(n)}
        for (u, v) in edges:
            G[u].append(v)
            G[v].append(u)

        vis = set()
        to_explore = [source]
        while to_explore != []:
            cur_node = to_explore.pop()
            
            if cur_node in vis:
                continue


            if cur_node == destination:
                return True

            vis.add(cur_node)
            to_explore.extend(G[cur_node])

        return False


            



        
        