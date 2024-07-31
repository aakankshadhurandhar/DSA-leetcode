class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        minValue=min(bloomDay)
        maxValue=max(bloomDay)
        minDays=float('inf')
        while minValue<=maxValue:
            count=0
            bouquets=0
            mid=minValue+(maxValue-minValue)//2
            for j in range(len(bloomDay)):
                if bloomDay[j]<=mid:
                    count+=1
                else:
                    count=0
                if count>=k:
                    bouquets+=1
                    count=0
            if bouquets>=m:
                minDays=min(minDays,mid)
                maxValue=mid-1
            else:
                minValue=mid+1
        return minDays if minDays!=float('inf') else -1
                
            

        