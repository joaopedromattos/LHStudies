class Solution:
    def isValid(self, s: str):
        if s == '':
            return True
        
        if not s:
            return False
        
        stack = []
        possibilities = {
            '[' : ']',
            '(' : ')',
            '{' : '}'
        }
        
        for cur_char in s:
            if cur_char in '])}':
                if stack == []:
                    return False
                
                popped_char = stack.pop()
                if possibilities[popped_char] != cur_char:
                    return False
            else:
                stack.append(cur_char)
                
        if stack != []:
            return False
            
        return True
            