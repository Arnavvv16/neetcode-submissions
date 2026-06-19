class Solution:
    def dfs(self, r,c, rows, cols, grid , visited):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] == 1:
            return
        if grid[r][c]== "0":
            return 
    
        visited[r][c] = 1
        self.dfs(r+1, c, rows , cols, grid, visited)
        self.dfs(r-1, c, rows , cols, grid, visited)
        self.dfs(r, c+1, rows , cols, grid, visited)
        self.dfs(r, c-1, rows , cols, grid, visited)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        cnt = 0 
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c] == "1" :
                    self.dfs(r,c, rows,cols, grid, visited)
                    cnt = cnt + 1 

        return cnt
