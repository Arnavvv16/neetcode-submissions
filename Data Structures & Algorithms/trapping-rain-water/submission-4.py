class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # suffix max precomputation
        suffixmax = [0]*n
        currentmax = float("-inf")
        for i in range(n-1,-1,-1):
            currentmax = max(height[i],currentmax)
            suffixmax[i]=currentmax
        
        area = 0
        prefixmax= 0 # greatest on left side
        for i in range(0, n):
            prefixmax= max(height[i],prefixmax)
            area = area + min(prefixmax, suffixmax[i]) - height[i]
        return area
#  this was in o(n) for tc,sc 
# optimal is in o(n) time and o(1) space using 2 pointers

        '''n = len(height)
        # suffix max precomputation
        suffixmax = [0]*n
        currentmax = float("-inf")
        for i in range(n-1,-1,-1):
            currentmax = max(height[i],currentmax)
            suffixmax[i]=currentmax
        
        area = 0
        prefixmax= 0 # greatest on left side
        for i in range(0, n):
            prefixmax= max(height[i],prefixmax)
            area = area + min(prefixmax, suffixmax[i]) - height[i]
        return area'''
