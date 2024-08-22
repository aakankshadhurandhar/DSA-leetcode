class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax,rightmax=0,0
        l,r=0,len(height)-1
        result=0
        while l < r:
            leftmax,rightmax=max(leftmax,height[l]),max(rightmax,height[r])
            if height[l]<height[r]:
                result+=leftmax-height[l]
                l+=1
            else:
                result+=rightmax-height[r]
                r-=1
        return result
            

             


        