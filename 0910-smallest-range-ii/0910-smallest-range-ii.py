class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_range = nums[n - 1] - nums[0]

        for i in range(1, n):
            max_val = max(nums[i - 1] + k, nums[n - 1] - k) 
            min_val = min(nums[0] + k, nums[i] - k) 

         
            min_range = min(min_range, max_val - min_val)

        return min_range
