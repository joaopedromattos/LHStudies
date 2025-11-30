'''
In: int
Out: bool

Test case:

c = 10
True, because 1 ** 2 + 3 ** 2 = 10


c - (c - (a ** 2)) = a ** 2


c = a ** 2 + (c - a**2)

Principle: Every number between 0 and c // 2 + the sqrt of the complement should satisfy. Our answer is the complement that is a perfect square.

One possible algorithm
for every a
    - check if (c - a**2) is a perfect square


0 --------------------- c // 2
   a                b


Time : O((c // 2)logn)

Space: O(1)



'''

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1:
            return True

        if c == 0:
            return True

        for i in range(math.isqrt(c) + 1):
            b = i
            l, h = 0, int(math.isqrt(c))

            while h - l > 1:
                m = (h + l) // 2

                if (m**2) > c - (b ** 2):
                    h = m
                else:
                    l = m

            if (l ** 2) + (b ** 2) == c:
                return True

            if (h ** 2) + (b ** 2) == c:
                return True

        return False

            



        