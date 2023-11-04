class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        val = []
        mp = defaultdict()
        n = len(nums)
        for i in range(n):
            mp[nums[i]] = nums[i] * nums[i]
        
        for i in range(n):
            val.append(mp[nums[i]])
        return sorted(val)
            
        
        