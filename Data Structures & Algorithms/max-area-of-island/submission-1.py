class Solution:
    def dfs(self, r,c, rows, cols, grid , visited):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if visited[r][c] == 1:
            return 0
        if grid[r][c]== 0:
            return 0
    
        visited[r][c] = 1
        area = 1 
        area += self.dfs(r+1, c, rows , cols, grid, visited)
        area += self.dfs(r-1, c, rows , cols, grid, visited)
        area += self.dfs(r, c+1, rows , cols, grid, visited)
        area += self.dfs(r, c-1, rows , cols, grid, visited)
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        maxarea = 0
        area = 0
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c] == 1 :
                    islandarea = self.dfs(r,c, rows,cols, grid, visited)
                    maxarea = max(maxarea,islandarea)

                    

        return maxarea

    
        