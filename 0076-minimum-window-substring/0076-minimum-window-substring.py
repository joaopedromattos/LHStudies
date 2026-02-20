'''

Principle: If you check a substring with 1 character, you can expand it until it is valid. and go through the string with only the valid substrings.


given a window, check if it is valid
    - if yes, check if we can reduce from left
    - if not, expand and update

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        i, j = 0, 1
        sub_count = Counter(s[i:j])
        how_many_satisfied = (sub_count[s[j-1]] == t_count[s[j-1]])


        smallest_ans = inf
        smallest_i, smallest_j = None, None

        isValid = sub_count == t_count

        
        while i < len(s) or j < len(s):

            # print(s[i:j])
            if not isValid:

                if j == len(s):
                    break


                j += 1
                
                sub_count[s[j-1]] += 1
                how_many_satisfied += (sub_count[s[j-1]] == t_count[s[j-1]])

                isValid = (how_many_satisfied >= len(t_count)) and (sub_count[s[j-1]] >= t_count[s[j-1]])

                
            else:

                if len(s[i:j]) < smallest_ans:
                    smallest_i, smallest_j = i, j
                    smallest_ans = len(s[i:j])
                    
                how_many_satisfied -= (sub_count[s[i]] == t_count[s[i]])
                
                sub_count[s[i]] -= 1
                
                isValid = (how_many_satisfied >= len(t_count)) and (sub_count[s[i]] >= t_count[s[i]])
                
                i += 1


        if smallest_i == None and smallest_j == None:
            return ""

        else:
            return s[smallest_i:smallest_j]


                
        