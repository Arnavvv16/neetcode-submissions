from collections import deque
class Solution: #using bfs now
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        atlantic = set()
        pacific = set()

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 :
                    queue.append((r,c, heights[r][c]))
                    pacific.add((r,c))

        while queue:
            a,b, h = queue.popleft()
            if a<0 or a >= rows or b < 0 or b >= cols:
                continue
               
            for x,y in [[1,0], [-1,0], [0,1], [0,-1]]:
                newi = a + x
                newj = b + y
                if newi < 0 or newj < 0 or newi>=rows or  newj>=cols:
                    continue
                if heights[newi][newj] >= h and (newi,newj) not in pacific:
                    pacific.add((newi,newj))
                    queue.append((newi,newj, heights[newi][newj]))
        
        for r in range(rows):
            for c in range(cols):
                if r == rows-1  or c == cols-1 :
                    queue.append((r,c, heights[r][c]))
                    atlantic.add((r,c))
        while queue:
            a,b, h = queue.popleft()
            if a<0 or a >= rows or b < 0 or b >= cols:
                continue
            for x,y in [[1,0], [-1,0], [0,1], [0,-1]]:
                newi = a + x
                newj = b + y
                if newi < 0 or newj < 0 or newi>=rows or  newj>=cols:
                    continue
                if heights[newi][newj] >= h and (newi,newj) not in atlantic:
                    atlantic.add((newi,newj))
                    queue.append((newi,newj, heights[newi][newj]))

        common =[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    common.append([r,c])

        return common 

