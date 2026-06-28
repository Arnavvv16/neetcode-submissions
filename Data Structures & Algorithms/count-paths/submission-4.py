class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # prev represents the row above, curr represents the current row
        prev = [0 for _ in range(n)]
        curr = [0 for _ in range(n)]
        
        # Base case: 1 way to be at the starting cell
        prev[0] = 1
        
        # Fill the grid row by row
        for up in range(m):
            # For the very first row, curr is the same as prev's initialized state
            if up == 0:
                curr[0] = 1
            else:
                curr[0] = prev[0] # The first column only gets paths from above
                
            for do in range(n):
                # Skip the starting cell
                if up == 0 and do == 0:
                    continue
                    
                # Look at the cell directly above (from the previous row array)
                if up > 0:
                    from_above = prev[do]
                else:
                    from_above = 0
                    
                # Look at the cell to the left (from the current row array)
                if do > 0:
                    from_left = curr[do-1]
                else:
                    from_left = 0
                
                # Total paths to the current cell
                curr[do] = from_above + from_left
                
            # Move to the next row: the current row becomes the previous row
            prev = list(curr)
            
        # The last element in our final row holds the answer
        return prev[n-1]