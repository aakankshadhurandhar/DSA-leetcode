class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        """
        n 
        queries
        queriesp[i]=[li,ri]
        select subset of indices within range[li,ri] in nums
        decrement values at selected indices -1
        
        zero array-> all elements =0
        true
        
        [1,0,1]
        [0,2]
        
        0,1,2
        -> 0,0,0
        Brute force 
        1. loop over nums
        2. loop over queries
        3. slice off arr=[li,ri]
        4. run loop over arr:
                arr[i]-=1
        return all(elements are 0) return true else false
        
        Optimise:
        
        1,0,1
        
        0 1 2
        map : indices : value
        loop : queries 
        indices : -1
        
        0 -> 1
        1 -> 0
        2 -> 1
        
        0 1 2 3 4 5 6
        1     0 0 0 -1
        1 1 1 1 1 1 0
        
        queries: [0,2],[0,2]
        li -> ri
        sub[n+1]
        sub[0]=2;
        sub[1]=2;
        sub[2]=2;
        sub[3]=0;
        
        for query in queries:
            l = 0;
            r = 2;
            sub[0]++;
            sub[3]--;
        
        for i in range(1,n+1):
            sub[i] = sub[i-1] + sub[i]
           
           nums[i]=5, sub[i]=6 : 
 
        """
        n=len(nums)
        
        sub=[0 for _ in range(n+1)]
        for li,ri in queries:
            sub[li]+=1
            sub[ri+1]-=1
        
        for i in range(1,n):
            sub[i]=sub[i-1]+sub[i]
        for i in range(n):
            if nums[i]>sub[i]:
                return False
     
        return True
        
        
        
        