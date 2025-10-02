'''
verify there's a node for all v in V, 

N = 4
trust -> [[1,4], [2, 4], [3, 4], [2, 3], [1, 2]]

Trust graph
1:[]
2:[]
..
4: [1, 2, 3] -> num_nodes - 1

Trusted graph
1: [4]
2: [4]
...
4: [] 

Time -> O(E + 2N), O(2N + E)


'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1:
            return 1

        trust_G = {i : [] for i in range(1, n + 1)} # k : []
        trust_me_G = {i : [] for i in range(1, n + 1)} # k : []

        for (u, v) in trust:
            trust_G[u].append(v)
            trust_me_G[v].append(u)

        judge = -1
        for i in range(1, n + 1):
            if (trust_G[i] == []) and (len(trust_me_G[i]) == n-1):
                return i

        return judge


        