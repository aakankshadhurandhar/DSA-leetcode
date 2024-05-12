class Solution(object):
    def doOverlap(self,interval1,interval2):
         front = max(interval1[0], interval2[0])
         back = min(interval1[1], interval2[1])
         return back - front >= 0
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            interval2=result[-1]
            if self.doOverlap(intervals[i],interval2):
                merged_front=min(intervals[i][0],interval2[0])
                merged_back=max(intervals[i][1],interval2[1])
                result[-1]=[merged_front,merged_back]
            else:
                result.append(intervals[i])
        return result



        