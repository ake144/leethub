class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        a = set(nums1)
        b = set(nums2)
        for i in a:
            for j in b:
                if i == j :
                    arr.append(i)
        return arr
        