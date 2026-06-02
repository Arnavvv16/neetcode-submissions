class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i =0 
        j = n-1 
        maxarea = float("-inf")

        while i<j :
            area = min(heights[i],heights[j]) * (j-i)
            maxarea = max(maxarea,area)
            if heights[i] < heights [j]:
                i = i +1
            else:
                j = j-1
            
        return maxarea