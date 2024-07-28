class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        
        queue=deque()
        fresh_oranges=0
        min_minutes=0
        rows=len(grid)
        col=len(grid[0])
        for i in range(rows):
            for j in range(col):
                if grid[i][j]==2:
                    # append minminutes at that time
                    queue.append((i,j,0))
                if grid[i][j]==1:
                    fresh_oranges+=1
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh_oranges:
            min_minutes += 1
            for _ in range(len(queue)):
                x,y,minutes=queue.popleft()


                for dx,dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<rows and 0<=ny<col and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        fresh_oranges-=1
                        queue.append((nx,ny,min_minutes+1))
        return min_minutes if fresh_oranges == 0  else -1
        



                

        
        