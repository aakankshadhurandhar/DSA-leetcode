from collections import deque

class Solution(object):
    def bfs(self, visited, queue, row, col, heights):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for r, c in directions:
                nr, nc = x + r, y + c
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and heights[nr][nc] >= heights[x][y]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []

        row, col = len(heights), len(heights[0])
        visited_pacific = [[0 for _ in range(col)] for _ in range(row)]
        visited_atlantic = [[0 for _ in range(col)] for _ in range(row)]
        queue_pacific = deque()
        queue_atlantic = deque()
        res = []

        # Vertical left and right border
        for i in range(row):
            queue_pacific.append((i, 0))
            queue_atlantic.append((i, col - 1))
            visited_pacific[i][0] = 1
            visited_atlantic[i][col - 1] = 1

        # Top and bottom border
        for j in range(col):
            queue_pacific.append((0, j))
            queue_atlantic.append((row - 1, j))
            visited_pacific[0][j] = 1
            visited_atlantic[row - 1][j] = 1

        self.bfs(visited_pacific, queue_pacific, row, col, heights)
        self.bfs(visited_atlantic, queue_atlantic, row, col, heights)

        for i in range(row):
            for j in range(col):
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    res.append([i, j])

        return res
