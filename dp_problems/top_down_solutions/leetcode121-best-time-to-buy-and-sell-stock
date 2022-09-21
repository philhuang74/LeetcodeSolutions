class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        
        def dp(i, transactions, hold_stock):
            if transactions == 0 or i == days:
                return 0
            if (i,transactions,hold_stock) not in memo:
                profit_do_nothing = dp(i+1, transactions, hold_stock)
                if hold_stock:
                    profit_act = dp(i+1,transactions-1, False) + prices[i]
                else:
                    profit_act = dp(i+1, transactions, True) - prices[i]
                memo[(i,transactions,hold_stock)] = max(profit_do_nothing, profit_act)
            return memo[(i,transactions,hold_stock)]
        
        memo = {}
        return dp(0, 1, False)
