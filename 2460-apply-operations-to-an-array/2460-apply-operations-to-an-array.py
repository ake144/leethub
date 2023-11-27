class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i,j = 0,1 
        while j < len(nums):
            if nums[i] == nums[j] and nums[i] != 0:
                nums[i] += nums[j]
                nums[j] = 0
                i += 2 
                j = i + 1
            else:
                i += 1
                j += 1
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j +=1
            
        return nums
        
        