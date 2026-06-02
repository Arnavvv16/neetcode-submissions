class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        n = len(nums)
        res = []
        while i < n-k+1 :
            maxx = float("-inf")
            for j in range(i, i+k):
                maxx = max(maxx,nums[j])
        
            res.append(maxx)
            i += 1
        return res


        
            
            