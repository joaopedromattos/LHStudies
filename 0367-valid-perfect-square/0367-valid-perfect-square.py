'''

In: int
output: bool


10 -> False -> because 3*3 < sqrt(10) < 4*4 

Principle: One can approximate by the sqrt of a number, by finding subsequent halves. (Induction)


Time: O(logn) Space O(1) (Not considering inputs)

'''



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a, b = 0, num

        if num == 1:
            return True

        if num == 0:
            return False

        while b - a > 1:
            m = (b+a) // 2

            if m * m > num:
                b = m
            else:
                a = m

        return (a * a == num) or (b * b == num)
        