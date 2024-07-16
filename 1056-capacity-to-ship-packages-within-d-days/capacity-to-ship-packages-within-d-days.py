class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        minvalue=max(weights)
        maxvalue=sum(weights)
        while minvalue<=maxvalue:
            days_needed=1
            currentload=0
            mid=minvalue+(maxvalue-minvalue)//2
            for weight in weights:
                if currentload+weight<=mid:
                    currentload+=weight
                else:
                    days_needed+=1
                    currentload=weight
                    if days_needed>days:
                        break
            if days_needed<=days:
                maxvalue=mid-1
            else:
                minvalue=mid+1
        return minvalue
        