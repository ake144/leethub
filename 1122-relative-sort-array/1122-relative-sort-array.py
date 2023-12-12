class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arranged = []
        for  num in arr2:
            while num in arr1:
                arranged.append(num)
                arr1.remove(num)
                
        return  arranged + sorted(arr1)             
        
                
        