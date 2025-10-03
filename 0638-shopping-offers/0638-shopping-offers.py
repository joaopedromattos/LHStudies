from typing import List
from functools import lru_cache
from math import inf

class Solution:
    
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        n = len(price)

        @lru_cache(None)
        def backtracking(items_we_bought: tuple, accum_price: int) -> int:
            items_we_bought = list(items_we_bought)

            if items_we_bought == needs:
                return accum_price

            # Best cost: buying remaining items individually
            min_cost = accum_price + sum((needs[i] - items_we_bought[i]) * price[i] for i in range(n))

            # Try ALL deals, not just the “best one”
            for deal in special:
                valid = True
                new_items = items_we_bought[:]
                for i in range(n):
                    if new_items[i] + deal[i] > needs[i]:
                        valid = False
                        break
                    new_items[i] += deal[i]
                if valid:
                    min_cost = min(min_cost, backtracking(tuple(new_items), accum_price + deal[-1]))

            return min_cost

        return backtracking(tuple([0] * n), 0)
