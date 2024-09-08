import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
       
        l = 1
        high = max(piles)
        ans = -1

        def checkHrs(mid, piles):
            hrs = 0
            for pile in piles:
                hrs += (pile + mid - 1) // mid  # Equivalent to ceil(pile / mid)
            return hrs

        while l <= high:
            mid = (l + high) // 2
            hrs = checkHrs(mid, piles)

            if hrs <= h:
                ans = mid
                high = mid - 1
            else:
                l = mid + 1
        
        return ans
     