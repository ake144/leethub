class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        missing = duplicate=-1
        for i in range(1,n+1):
            if counter[i] == 2:
                duplicate = i
            elif counter[i] == 0:
                missing = i
        return [duplicate,missing]

                
                
        
        