class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1 or n == 2:
            return 1
        trib_list = [0] * (n+1)
        trib_list[1] = trib_list[2] = 1
        for i in range(3,n+1):
            trib_list[i] = trib_list[i-3] + trib_list[i-2] +trib_list[i-1]
        return trib_list[n]
        
