class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        line=[0]*102
        for i in nums:
            line[i[0]]+=1
            line[i[1]+1]-=1
        count=0
        ans=0
        for p in range(102):
            count+=line[p]
            if count>0:
                ans+=1
        return ans
        