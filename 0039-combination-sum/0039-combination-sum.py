# [1, 2,3, 4] , target = 3


# 1, R: 2 [1, 2, 3, 4]
# 1, R: 1 or 2, R:0 (A)
# 1, R:0 (A)


# 2, R:1
# 1, R:0 (ND)

# 3, R:0 (A)

# 4: R: -1 (X)


# Time -> O(Target * N) / Space O(Target * N)
from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combs = []

        def backtracking(remaining, curr_combinations:Counter, global_index):
            if remaining == 0:
                combs.append(curr_combinations[:])
                return

            if remaining < -1:
                return

            for idx, i in enumerate(candidates[global_index:]):
                curr_combinations.append(i)
                backtracking(remaining - i, curr_combinations, global_index + idx)
                curr_combinations.pop()

        for idx, candidate in enumerate(candidates):
            backtracking(target - candidate, [candidate], idx)

        print(combs)
        return list(combs)

        

            

                
