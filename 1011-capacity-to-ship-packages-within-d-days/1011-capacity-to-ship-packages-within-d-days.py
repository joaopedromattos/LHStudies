'''
In: weights -> weights of each package (List[Int]), days => how many days do we have to ship all packages.

- Can we break a package into multiple days?

Principle: w => BIG_INT, days = 1
            w -> 0 -> number of days it takes to transport all weights: 
            [1,2, 7, 4, 5, 6, 7], w => 7 -> 8 days


            |000000000000000011111111111111|
            W=0                 W=100000000000
            
            
Binary search => O(weights * log n)




'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def can_carry(k):
            cur_days = 1
            accum_weight = 0
            i = 0
            while i < len(weights):
                cur_weight = weights[i]
                if cur_weight > k:
                    return False

                if cur_weight <= k - accum_weight:
                    accum_weight += cur_weight
                    i += 1
                else:
                    accum_weight = 0
                    cur_days += 1
            print('-' * 10)
            return cur_days <= days


        l, h = 0, 10_000_000_000

        while h - l > 1:
            mid = (h + l) // 2

            if can_carry(mid):
                h = mid
            else:
                l = mid

        return h


        