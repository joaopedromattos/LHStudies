'''
In: str, str -> length of the longest common subsequence

abcde, ade => 3 -> a __ de / ade 

ab___abcde, abcde => 5

a___b___c___d___e, a__d__e => 3


- Can A and B strings be empty? 
- Does A and B contain repeated characters?

Principle: For pointers (i, j) for each string, we have that we can break into subproblems, and combine them recursively (induction -> dynnamic programming)

Complexity => O(2 ** (len(A) + len(B)) -> O(len(A) * len(B))
Space => O(A * B)

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) == 0 or len(text2) == 0:
            return 0

        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            longest_subsequence = 0
            if text1[i] == text2[j]:
                return dp(i + 1, j + 1) + 1
        
            longest_subsequence += max(dp(i + 1, j), dp(i, j + 1))
            
            return longest_subsequence

        return dp(0,0)
        