'''
In: list[list[int]], flight[i] = [s, e, p]
Out: int

- Questions to the interviewer: Can we consider there are no negative prices?

Test case 1: 
src = 0, dest = 3
[[0, 1, 300], [0, 2, 350], [0, 3, 1000], [1, 3, 300], [2, 3, 50]]

0->1 300
1->3 300
---

0->2 350 -> Greedy will not always work!
2->3 50

---

0->3 1000


Principle: (Induction) The path we are finding is the path that minimizes the *sum up* to node dest is the path that minimizes the *sum* from src to i and from i to dest. i can be any node in between.


Algo:
while: explore next not empty
node = get next node to explore
-> Visit node
    -> add all neighbors to ("explore next", "prefix sum") list.
    mark cur node as visited.
    

Time: O(E)
Space: O(N + E)
'''

import heapq



from bisect import insort_left

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        G = [[] for i in range(n)]
        
        for s, d, p in flights:
            G[s].append((d, p))
    
        explore = deque([(0, src, 0)])

        vis = dict(zip(range(n), [inf] * n))
        cur_steps = 0
        while explore:
            cur_price, cur_node, num_steps = explore.popleft()

            for neigh, price in G[cur_node]:
                
                if num_steps < k + 1:
                    if price + cur_price < vis[neigh]:
                        explore.append((price + cur_price, neigh, num_steps + 1))
                        vis[neigh] = price + cur_price

        return vis[dst] if vis[dst] != inf else -1