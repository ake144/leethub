class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count= 0
        i,j = 0,1
        while j < len(nums)-1:
            if (nums[i] < nums[j] and nums[j] > nums[j + 1]) or (nums[i] > nums[j] and nums[j] < nums[j + 1]):
                count += 1
                i  = j
            j += 1           
        return count
                    
        
        