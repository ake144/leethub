class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        mid = (n + 1) // 2
        j, k = mid - 1, n - 1

        for i in range(0, n, 2):
            nums[i] = sorted_nums[j]
            j -= 1

        for i in range(1, n, 2):
            nums[i] = sorted_nums[k]
            k -= 1
                