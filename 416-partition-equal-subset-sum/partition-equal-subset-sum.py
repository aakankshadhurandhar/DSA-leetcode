class Solution(object):
    def solve(self,nums,i,target,dp):
        if target==0:
            return True
        if i>= len(nums) or target<0:
            return False
        if dp[i][target]!=-1:
            return dp[i][target]
        
        dp[i][target]=self.solve(nums,i+1,target-nums[i],dp) or self.solve(nums,i+1,target,dp)
        return dp[i][target]

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numssum=sum(nums)
        if numssum%2!=0:
            return False
        dp = [[-1 for _ in range(numssum // 2 + 1)] for _ in range(len(nums))]

        return self.solve(nums,0,numssum//2,dp)
        
        