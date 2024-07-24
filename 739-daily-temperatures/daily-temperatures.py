class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[[temperatures[0],0]]
        results=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                results[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            stack.append([temperatures[i],i])
        return results
        

        