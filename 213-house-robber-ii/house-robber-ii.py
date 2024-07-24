class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp1=[-1 for _ in range(n+1)]
        dp2=[-1 for _ in range(n+1)]
        def solve(nums,n,dp):
            
            if n < 0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            dp[n]=max(solve(nums,n-1,dp),solve(nums,n-2,dp)+nums[n])
            return dp[n]

        if n==1:

            return nums[0]
        return max(solve(nums[:-1],n-2,dp1),solve(nums[1:],n-2,dp2))