class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        maxarea = 0
        
        def dfs(r, c):
            # Base cases: out of bounds, already visited, or water (0)
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                visited[r][c] == 1 or 
                grid[r][c] == 0):
                return 0
            
            # Mark the current cell as visited
            visited[r][c] = 1
            
            # Count this cell (1) + the area from all 4 directions
            return (1 + 
                    dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                # If we find unvisited land, calculate its full area
                if grid[r][c] == 1 and visited[r][c] == 0:
                    maxarea = max(maxarea, dfs(r, c))
                    
        return maxarea