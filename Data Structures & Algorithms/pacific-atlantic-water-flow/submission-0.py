class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        atlantic = set()
        pacific = set()


        def dfs(r, c, ocean , prevheight ):
            if r < 0 or r >= rows or c < 0 or c>= cols:
                return
            if (r,c) in ocean: #o 1 lookup
                return 
            if heights[r][c] < prevheight :
                return 
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        # for both 
        for r in range(rows): # cols is zero:
            dfs(r , 0 , pacific, heights[r][0])
            dfs(r, cols -1 , atlantic, heights[r][cols-1])
        for c in range(cols): # rows is zero
            dfs(0,c, pacific, heights[0][c])
            dfs(rows -1, c, atlantic, heights[rows-1][c])

    
        common =[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    common.append([r,c])

        return common           
