class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        candidates.sort()
    
        
        def helper(start, temp, target):
            
            if target == 0:
                res.append(temp[:])
                return
            
            if start == len(candidates):
                return
            
            for i in range(start, len(candidates)):
                if(candidates[start] > target):
                    break
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                helper(i + 1, temp, target - candidates[i])
                temp.pop()
                
                
        helper(0, [], target)
        
        return res