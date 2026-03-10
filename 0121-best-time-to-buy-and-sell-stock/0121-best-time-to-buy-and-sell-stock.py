'''
In: List[Int], Out: Int

[1 2 3 4 5 6]
[1 2 -1000 4 5 6]

[1 2 -1000 4 5 -1000]

Principle: Find the first day, after the "minimum" = 0, then stop at the last day before the "minimum" = 0.
    - Pre-fix sum


[1 2 0 4 5 0]
 0 1  3. 3 4   5



'''


# class Solution: 
#     def maxProfit(self, prices: List[int]) -> int:

#         pfs = [0] * (len(prices) + 1)
#         for i in range(1, len(prices)):
#             pfs[i] = pfs[i-1] + prices[i-1]

#         print(pfs)

#         start = 0
#         max_profit = -1
#         for i in range(1, len(pfs)):
#             if pfs[i] < pfs[start]:
#                 start = i
            
#             if pfs[i] - pfs[start] >  max_profit:
#                 end = i
                

#         return prices[end - 1] - prices[start]

        
# [1 2 0 4 5 0]
#  1 1 1 0 0 0

class Solution: 
    def maxProfit(self, prices: List[int]) -> int:

        min_so_far = inf
        max_profit = 0
        for price in prices:
            if price < min_so_far:
                min_so_far = price

            max_profit = max(price - min_so_far, max_profit)

        return max_profit