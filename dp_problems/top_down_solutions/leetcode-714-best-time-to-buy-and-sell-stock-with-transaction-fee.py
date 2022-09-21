class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        days = len(prices)
        def dp(i, hold_stock):
            if i == days:
                return 0
            if (i,hold_stock) not in memo:
                profit_do_nothing = dp(i+1, hold_stock)
                if hold_stock:
                    profit_act = dp(i+1, False) + prices[i] - fee
                else:
                    profit_act = dp(i+1, True) - prices[i] 
                memo[(i,hold_stock)] = max(profit_do_nothing, profit_act)
            return memo[(i,hold_stock)]
        memo = {}
        return dp(0, False)
                
