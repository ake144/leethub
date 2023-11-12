class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums)> 1:
            md = (len(nums) // 2)
            L = nums[:md]
            R = nums[md:]
            
            self.sortArray(L)
            self.sortArray(R)
            i=j=k= 0
            while i < len(R) and j < len(L):
                if R[i] <= L[j]:
                    
                    nums[k] = R[i]
                    i += 1
                else:
                    nums[k] = L[j]
                    j+= 1
                k += 1
            while i < len(R):
                nums[k] = R[i]
                i += 1
                k+= 1
            while j < len(L):
                nums[k] = L[j]
                j += 1
                k += 1
                
        return nums
        