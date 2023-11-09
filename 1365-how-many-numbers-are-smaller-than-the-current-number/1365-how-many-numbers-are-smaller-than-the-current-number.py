class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        count = []
        for i in range(len(nums)):
            a= nums[i]
            for j in range(len(nums)):
                if (nums[j] < a) and j != i:
                    arr.append(nums[j])
                    
                
                
            
            count.append(len(arr))
            arr = []
        print(arr)            
                
                
        return count
        
        