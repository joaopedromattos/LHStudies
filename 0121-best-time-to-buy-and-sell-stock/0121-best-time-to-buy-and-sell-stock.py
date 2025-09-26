class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [7,1,5,3,6,4]

        high, low, profit = prices[0], prices[0], 0
        if not prices:
            return 0

        # Logic
        for cur_price in prices:
            if cur_price < low:
                low = cur_price
                high = low
            
            if cur_price > high and cur_price - low > profit:
                
                high = cur_price
                profit = high - low

        profit = max(profit, 0)
        
        return profit




        