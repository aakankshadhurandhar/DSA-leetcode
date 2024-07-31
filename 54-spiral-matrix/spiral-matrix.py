class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        s=0
        row=len(matrix)
        col=len(matrix[0])
        ans=[]
        while s<row and s<col:
            #top left to right
            for i in range(s,col):
                ans.append(matrix[s][i])
            #top right to bottom
            for j in range(s+1,row):
                ans.append(matrix[j][col-1])
            #bottom top to right
            if s + 1 < row:
                for i in range(col-2, s-1, -1):
                    ans.append(matrix[row-1][i])
            if s + 1 < col:
                for j in range(row-2, s, -1):
                    ans.append(matrix[j][s])
            s += 1
            row -= 1
            col -= 1
        return ans





        