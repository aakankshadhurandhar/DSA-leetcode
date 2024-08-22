class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        maxarea=0
        while l<r:
            h=min(height[l],height[r])
            area=h*(r-l)
            maxarea=max(area,maxarea)
            print(area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea
        