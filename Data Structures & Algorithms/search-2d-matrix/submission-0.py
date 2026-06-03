class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        
        top = 0
        bottom = r -1

        while top<= bottom :
            m = (top+bottom)//2
            if target < matrix[m][0] :
                bottom = m -1 
            elif target > matrix[m][c-1]:
                top = m + 1
            else:
                break 
    
        if top > bottom :
            return False 
        
        left = 0 
        right = c-1 
        while left <= right :
            m2 = (left + right)//2
            if target == matrix[m][m2]:
                return True
            if target > matrix[m][m2]:
                left  = m2 +1 
            if target < matrix[m][m2]:
                right = m2 -1 
        return False 










