class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) < 2:
                a = nums[i]
        return a