class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        l,r=min(time),min(time)*totalTrips
        while l<r:
            actualTrips=0
            mid=l+(r-l)//2
            for i in range(len(time)):
                actualTrips+=mid/time[i]
            if actualTrips < totalTrips:
                l=mid+1
            else:
                r=mid
        return l

        