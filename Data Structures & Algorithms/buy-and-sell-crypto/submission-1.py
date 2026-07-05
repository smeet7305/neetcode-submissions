class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        max_profit=0

        for s in range(len(prices)):
            profit=prices[s]-prices[b]
        
            if prices[s]<prices[b]:
                b=s
        
            max_profit=max(profit,max_profit)
    
        return max_profit

        