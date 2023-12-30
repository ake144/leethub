class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
             return [-1,-1]
        n = len(nums)
        pos = -1
        left = 0
        l = -1
        r = -1
        right = n - 1
        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target:
                l = r = mid
                while l > 0 and nums[l - 1] == target:
                    l -= 1
                while r < n - 1 and nums[r + 1] == target:
                    r += 1
                return [l, r]
            elif nums[mid] < target: 
                left = mid + 1
            else:
                right = mid - 1

