class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''for i in range(0, len(nums)):
            if nums[i] == target:
                return i
        
        return -1 ''' #lol O(N) is chillin 

        n = len(nums)
        l = 0
        h = n-1

        while l<= h :
            m = (l+h)//2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target < nums[m] and target >= nums[l]:
                    h = m -1 
                else :
                    l = m +1 
                     

            elif nums[m] <= nums[h]:
                if target <= nums[h] and target > nums[m]:
                    l = m +1
                else :
                    h = m -1 
        return -1       
            
                

