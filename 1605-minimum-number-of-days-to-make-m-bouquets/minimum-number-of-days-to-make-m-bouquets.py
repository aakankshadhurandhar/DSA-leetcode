class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        minvalue=min(bloomDay)
        maxvalue=max(bloomDay)
        n=len(bloomDay)
        res=float("inf")
        while minvalue<=maxvalue :
            bouquets=0
            count=0
            mid=minvalue+(maxvalue-minvalue)//2
            for j in range(n):
                if bloomDay[j]<=mid:
                    count+=1
                else:
                    count=0
                if count>=k:

                    bouquets+=1
                    count=0
            if bouquets >= m:
                res=min(res,mid)
                maxvalue=mid-1
            else:
                minvalue=mid+1
        return res if res< float("inf") else -1
            
