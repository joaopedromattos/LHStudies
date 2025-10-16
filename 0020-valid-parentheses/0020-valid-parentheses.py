'''
In:
chars => [], (), {}

Out: bool

Test cases:
[({)]}
]{}[
]

Algo:
- go through string
- while string not fully consumed:
    - if char is {([ -> append to stack
    - if char is })] and matches to of the stack -> pop from stack
        - if fail to pop -> return false

if stack not empty -> return false

return true


Time : O(N) (N is the size of the string)
Space : O(M) -> How many 'open' chars we have e.g. ([{
'''

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False
            

        chars = {'(': ')',
                '[': ']',
                '{': '}'}
        

        stack = []
        c = 0
        while c < len(s):
            if s[c] in chars:
                stack.append(s[c])
            else:
                if stack:
                    if s[c] == chars[stack[-1]]:
                        # If current closing char
                        # matches top of the stack
                        stack.pop()
                    else:
                        return False 
                else:
                    # We found a closing char
                    # in an empty stack
                    return False

            c += 1

        if stack:
            # We processed all chars
            # and we did not close
            # all we opened
            return False

        return True

            