class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # suffix max precomputation
        '''suffixmax = [0]*n
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
#  this was in o(n) for tc,sc 
# optimal is in o(n) time and o(1) space using 2 pointers

        l, r = 0, n-1 
        leftmax = height[l]
        rightmax = height[r]
        area = 0
        while l < r :
            if leftmax < rightmax :
                l = l + 1
                leftmax = max(leftmax, height[l])
                area = area + leftmax - height[l]

            else :
                r = r -1 
                rightmax = max(rightmax, height[r])
                area = area + rightmax - height[r]
        return area



