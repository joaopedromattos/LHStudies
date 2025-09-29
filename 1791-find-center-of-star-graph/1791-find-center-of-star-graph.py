class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        candidates = set()
        candidates.update(edges[0])
        for edge in edges[:4]:
            print(candidates, edge, candidates.intersection(set(edge)))
            candidates = candidates.intersection(set(edge))
        return list(candidates)[0]