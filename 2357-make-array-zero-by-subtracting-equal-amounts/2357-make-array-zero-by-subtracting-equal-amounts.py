class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        number_to_be_operated = (set(nums)-{0})
        return len((number_to_be_operated))
      

            
                
        