class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def recursive(i,dp):
            if i>len(s)-1:
                return True
            if i==len(s):
                return True
            if dp[i] is not None:
                return dp[i]
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict and recursive(j+1,dp):
                    dp[i]=True
                    return dp[i]
            dp[i]=False
            return dp[i]


        dp=[None]*(len(s)+1)
        return recursive(0,dp)
        