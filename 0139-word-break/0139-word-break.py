'''
In: s : String, wordDict : List[String]

s = 'abcefg' ['ab', 'ce', 'fz', 'wg'] -> Invalid
s = 'abcefg' ['abc', 'ce', 'fg', 'efg'] -> Valid


s = 'abcefg' ['ab', 'abc', 'cef', 'fg'] -> Valid

s = 'abcefg' ['a', 'ab', 'abc', 'abce', ] -> Valid



- What's the length of S, on average
- What's the length of wordDict on average? 
- What happens if the string is empty? Is it considered contained?

Principle: Find break points in S so that s_left and s_remaining can be found using wordDict.

Algo: 
- scan current S:
    - check if S in wordDict:
        - break S here and call the function again
    
return False -> True

Time: O((len(S) - 1) * len(S) / 2)
Space: O(len(S))
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        @cache
        def backtracking(cur_s):

            if len(cur_s) == 0:
                return True

            if len(cur_s) == 1:
                if cur_s in wordset:
                    return True
                else:
                    return False

            is_valid = False
            for i in range(1, len(cur_s) + 1):
                if cur_s[:i] in wordset:
                    is_valid = is_valid or (backtracking(cur_s[i:]) or (cur_s[i:] in wordset))

                    if is_valid:
                        return True
                    

            
            return False


        return backtracking(s)

        