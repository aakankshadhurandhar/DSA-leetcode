class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1 for _ in range(n+1)]
        def solve(x,dp):
            if x<0:
                return 0
            if x<=1:
                return 1
            if dp[x]!= -1:
                return dp[x]
            dp[x]= solve(x-1,dp)+solve(x-2,dp)
            return dp[x]
        return solve(n,dp)

        