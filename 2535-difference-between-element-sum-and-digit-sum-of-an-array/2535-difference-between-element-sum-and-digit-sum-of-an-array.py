class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        normal = 0
        for i in nums:
            normal += i
        inner = 0
        string_num = ''.join(map(str,nums))
        for i in string_num:
            inner += int(i)
        print(inner)
        return abs(normal - inner)