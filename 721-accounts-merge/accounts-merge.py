class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_accounts=defaultdict(list)
        visited=[False]*len(accounts)
        #make a graph
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                email=account[j]
                email_to_accounts[email].append(i)
        #dfs
        def dfs(i,emails):
            if visited[i]:
                return
            visited[i]=True
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for neighbour in email_to_accounts[email]:
                    dfs(neighbour,emails)








        #dfs on graph
        res=[]
        for i,account in enumerate(accounts):
            if visited[i]:
                continue 
            name,emails=account[0],set()
            dfs(i,emails)
            res.append([name]+ sorted(emails))
        return res



        