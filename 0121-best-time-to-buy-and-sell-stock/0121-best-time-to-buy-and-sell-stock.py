class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        best_profit = 0
        last_price = prices[0]
        curr_min = prices[0]
        curr_max = prices[0]
    
        for i in range(1, len(prices)):
            curr_price = prices[i]
            
            if curr_price > last_price:
                curr_max = curr_price
            elif curr_price < last_price:
                curr_max = curr_price
                curr_min = min(curr_min, curr_price)

            best_profit = max(best_profit, curr_max - curr_min)
            last_price = curr_price
        return best_profit
