class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        gridcopy = deepcopy(grid)
        minutes = 0
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if gridcopy[r][c] == 2:
                    queue.append([r,c])
                if gridcopy[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and queue:
            minutes +=1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in [[0,1], [0,-1], [-1,0], [1,0]]:
                    newi = i + dx 
                    newj= j + dy
                    if newi< 0 or newi == rows or newj < 0 or newj == cols:
                        continue 
                    if gridcopy[newi][newj] == 0 or gridcopy[newi][newj] == 2:
                        continue 
                    fresh -= 1
                    gridcopy[newi][newj] = 2 
                    queue.append([newi,newj])
        if fresh > 0:
            return -1
        return minutes
            