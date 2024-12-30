class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        best_profit = 0
        last_price = prices[0]
        local_min = prices[0]
    
        for i in range(1, len(prices)):
            curr_price = prices[i]

            # local_max = curr_price # We cannot sell in the past
            
            if curr_price < last_price:
                # But we can always buy now at a lower price!
                local_min = min(local_min, curr_price)

            # Save best profit
            best_profit = max(best_profit, curr_price - local_min)

            last_price = curr_price
        return best_profit
