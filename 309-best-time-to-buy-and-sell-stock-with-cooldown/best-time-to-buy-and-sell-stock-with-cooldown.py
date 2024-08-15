class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        def helper(ind, buy,dp):
            if ind >= n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]

            if buy == 1:
                # sell stock and move to next day after cooldown
                dp[ind][buy]= max(helper(ind + 2, 0,dp) + prices[ind], helper(ind + 1, 1,dp))
            else:
                dp[ind][buy]= max(helper(ind + 1, 1,dp) - prices[ind], helper(ind + 1, 0,dp))
            return  dp[ind][buy]

        n = len(prices)
        dp = [[-1] * 2 for _ in range(n + 1)]
        return helper(0, 0,dp)
  
        