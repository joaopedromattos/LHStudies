'''
In: s -> balanced -> only L and R, number of Ls and Rs has to match
Out: List[str] -> Max size len(s / 2)

Test cases:
'LRRLRL' -> LR, RL, RL
'RLLLRLLRRR' -> RL, LLRLLRRR
'LLRLRR' -> LLRLRR


Demonstration:
- String are always balanced.
- If you just count the number of L/Rs that passed, it is guaranteed, there will be the same amount of L/Rs later.
- The maximum number will be to *always* unpack substrings of balanced strings -> because the minimum is always the string itself.

Algo:
-> memory = 0
-> strs = []
-> Scan string:
    - If cur char is L -> memory -= 1
    - If cur char is R -> memory += 1
    - if memory == 0:
        strs.append(string[:cur_char])

return strs


Time O(N) -> N -> Length of the string
Space O(1) -> We will just use an integer
'''



class Solution:
    def balancedStringSplit(self, s: str) -> int:

        if not s:
            return 0

        c = 0
        memory = 0
        ans = 0
        while c < len(s):
            if s[c] == 'R':
                memory += 1
            if s[c] == 'L':
                memory -= 1

            if memory == 0:
                # substring is balanced
                ans += 1
            c+=1

        return ans
        
