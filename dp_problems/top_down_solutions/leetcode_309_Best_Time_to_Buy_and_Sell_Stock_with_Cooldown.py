class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        def dp(day, hold_stock):
            if day >= len(prices):
                return 0
            if (day, hold_stock) not in memo:
                profit_do_nothing = dp(day+1, hold_stock)
                if hold_stock:
                    profit_act = dp(day+2, False) + prices[day]
                else:
                    profit_act = dp(day+1, True) - prices[day]
                memo[(day, hold_stock)] = max(profit_do_nothing, profit_act)
            return memo[(day, hold_stock)]
        memo = {}
        return dp(0, False)
            
