class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums1)):
            found = False
            for j in range(len(nums2)-1):
                if nums1[i]==nums2[j]:
                    found  = True
                    next_max = -1
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            
                            next_max = nums2[k]
                            break
                    ans.append(next_max)
            if not found:
                    ans.append(-1)

                        

        return ans
                    
                
        