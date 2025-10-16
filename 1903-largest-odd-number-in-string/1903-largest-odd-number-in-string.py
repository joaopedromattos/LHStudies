'''
In: num -> str

Out: odd_num -> str

Test:
222222221 -> 222222221

......X______ 


221222222 -> 221

Explanation:
- If X the leftmost odd number, everything that comes before X is part of the biggest odd number.
- If _____ is composed only of even numbers, then .......X is the largest odd number.
- There will never be something like ___.....X______, since every prefix to the odd number will be part of the odd number.
- We can scan the string looking for the index of the rightmost odd number.



Time O(N)
Space(1) 
'''



class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd_number_idx = -1
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]

        return ""
        
        # if last_odd_number_idx == -1:
        #     return ""

        # return num[:last_odd_number_idx + 1]


        