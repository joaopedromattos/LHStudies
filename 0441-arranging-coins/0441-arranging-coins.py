
class Solution:
    def condition(self, k, n):
        return (k * (k + 1) // 2) > n

    def arrangeCoins(self, n: int) -> int:

        l, h = 0, n + 1

        while h - l > 1:
            m = (h + l) // 2

            if self.condition(m, n):
                h = m
            else:
                l = m

        return l

        