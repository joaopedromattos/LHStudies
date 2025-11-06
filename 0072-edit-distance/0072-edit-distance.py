'''

In: str1 -> str2
Output: int -> Minimum number of ways to transform
    b d e
a   
b
c      
         0   

Main principle -> suffixes are smaller subproblems. Solving smaller subproblems can be re-used to solve larger subproblem.


i -> position in string 1
j -> position in string 2

Algo:
for each char i:
    insert -> consume char from str2
    delete -> consume char from str1
    replace -> consume char from str1 and str 2


N**2 States
O(3 ** N) -> No memoization
O(N ** 2) -> W/ memoization

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n, m = len(word1), len(word2)

        @cache
        def dp(i, j):
            
            if i >= n and j >= m:
                return 0

            match = inf
            if (i < n) and (j < m):
                if word1[i] == word2[j]:
                    match = dp(i + 1, j + 1)

            # insert
            insert = inf
            if j < m:
                insert = dp(i, j + 1) + 1

            # delete
            delete = inf
            if i < n:
                delete = dp(i + 1, j) + 1

            # replace
            replace = inf
            if (i < n) and (j < m):
                replace = dp(i + 1, j + 1) + 1

            return min(insert, delete, replace, match)


        return dp(0, 0)



            
        