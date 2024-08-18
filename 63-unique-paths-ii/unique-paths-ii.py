class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def paths(i,j,dp,m,n):
            if i==0 and j==0 and obstacleGrid[i][j]==0:
                return 1
            
            if i<0 or j<0 or i>m-1 or j>n-1 or obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            #left or top
            dp[i][j]= paths(i-1,j,dp,m,n) + paths(i,j-1,dp,m,n)
            return dp[i][j]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return paths(m-1,n-1,dp,m,n)
        