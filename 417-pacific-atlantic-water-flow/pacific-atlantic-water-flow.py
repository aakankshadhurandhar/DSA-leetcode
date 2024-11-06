class Solution(object):
    def bfs(self,visited,queue,row,col,heights):
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            x,y=queue.popleft()
            for r,c in directions:
                nr,nc=x+r,y+c
                if 0<=nr<row and 0<=nc<col and not visited[nr][nc] and heights[nr][nc]>=heights[x][y]:
                    visited[nr][nc]=1
                    queue.append((nr,nc))


    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # visited set for both pacific and atlantic 
        # queue for both
        # left 

        if not heights:
            return []
        row,col=len(heights),len(heights[0])
        visited_pacific=[[0 for _ in range(col)] for _ in range(row)]
        visited_atlantic=[[0 for _ in range(col)] for _ in range(row)]
        pacific_queue=deque()
        atlantic_queue=deque()

        # top and left border
        for j in range(col):
            #top
            pacific_queue.append((0,j))
            atlantic_queue.append((row-1,j))
            visited_pacific[0][j]=1
            visited_atlantic[row-1][j]=1
        
        #left border
        for i in range(row):
            pacific_queue.append((i,0))
            visited_pacific[i][0]=1
            atlantic_queue.append((i,col-1))
            visited_atlantic[i][col-1]=1
        print(pacific_queue)
        print(atlantic_queue)
        self.bfs(visited_pacific,pacific_queue,row,col,heights)
        self.bfs(visited_atlantic,atlantic_queue,row,col,heights)
        res=[]
        print(visited_atlantic)
        print(visited_pacific)
        for i in range(row):
            for j in range(col):
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    res.append([i,j])
        return res

        


        





                
    
        
        