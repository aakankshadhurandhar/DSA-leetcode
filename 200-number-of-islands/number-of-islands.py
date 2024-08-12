class Solution(object):
    def dfs(self,visited_set,grid,i,j,rows,cols):

        if i<0 or j<0 or i>=rows or j>=cols:
            return
        if visited_set[i][j]==1 or grid[i][j]=='0':
            return 
        visited_set[i][j]=1
        #left
        self.dfs(visited_set,grid,i-1,j,rows,cols)
        self.dfs(visited_set,grid,i+1,j,rows,cols)
        self.dfs(visited_set,grid,i,j-1,rows,cols)
        self.dfs(visited_set,grid,i,j+1,rows,cols)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return
        rows=len(grid)
        cols=len(grid[0])
        visited_set=[[0 for _ in range(cols)]for _ in range(rows)]
        number_of_islands=0
        for i in range(rows):
            for j in range(cols):
                if visited_set[i][j]==0 and grid[i][j]=='1':
                    number_of_islands+=1
                    self.dfs(visited_set,grid,i,j,rows,cols)
        return number_of_islands


        
        