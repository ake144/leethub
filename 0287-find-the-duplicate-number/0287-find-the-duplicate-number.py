class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        duplicate = -1
        for i  in range(1,n+1):
            if counter[i] >= 2:
                duplicate =  i
        return duplicate