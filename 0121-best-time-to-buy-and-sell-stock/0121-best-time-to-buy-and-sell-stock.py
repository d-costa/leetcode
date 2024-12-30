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
            
            # But we can always buy now at a lower price!
            if curr_price < local_min:
                local_min = curr_price

            # Save best profit
            if curr_price - local_min > best_profit:
                best_profit = curr_price - local_min

            last_price = curr_price
        return best_profit
