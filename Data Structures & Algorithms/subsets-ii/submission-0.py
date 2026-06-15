class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def sol(ind, subset):
            if ind >= len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[ind])
            sol(ind+1, subset)
            subset.pop()
            while ind < len(nums)-1 and nums[ind]==nums[ind+1]:
                ind +=1
            sol(ind+1,subset)

        sol(0,[])
        return res