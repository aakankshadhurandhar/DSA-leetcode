class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*n
        def solve(n,nums,dp):
            if n<0:
                return 0
            if n==0:
                dp[0]=nums[0]
            if dp[n]!=-1:
                return dp[n]
            dp[n]=max(nums[n]+solve(n-2,nums,dp),solve(n-1,nums,dp))
            return dp[n]
        return solve(len(nums)-1,nums,dp)
            
        