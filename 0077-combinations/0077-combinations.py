# n = 3, k = 2 -> 1 2, 1 3, 3 2
# 
# 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def backtrack(start, comb):

            if len(comb) == k:
                res.append(comb.copy())
                return
                
            # Starting at start,
            # we don't need repetitions,
            # modify for permutations
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

            return

        backtrack(1, [])
        return res
        