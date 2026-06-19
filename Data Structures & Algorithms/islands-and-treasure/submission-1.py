from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        q = deque()
        lol = 2147483647
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c,0])
                    visited[r][c] == 1
        while q:
            i,j, dist = q.popleft()
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                newi , newj = i +x, j + y 
                if newi < 0 or newi >= rows or newj <0 or newj >= cols:
                    continue
                if visited[newi][newj]==1:
                    continue
                if grid[newi][newj] == -1:
                    continue
                if  grid[newi][newj] == lol :
                    k = dist +1 
                    grid[newi][newj] = k
                    q.append([newi,newj,k])
                    visited[newi][newj] = 1
        


                    

        