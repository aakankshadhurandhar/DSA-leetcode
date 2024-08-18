class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def paths(i,j,dp):
            if i==0 and j==0:
                return 1
            
            if i<0 or j<0 or i>m-1 or j>n-1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            #left or top
            dp[i][j]= paths(i-1,j,dp) + paths(i,j-1,dp)
            return dp[i][j]

        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return paths(m-1,n-1,dp)

        