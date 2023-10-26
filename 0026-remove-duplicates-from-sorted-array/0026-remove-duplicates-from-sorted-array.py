class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        a = set(nums)
        nums.clear()
        for i in a:
            nums.append(i) 
        nums.sort()
        return len(nums)
