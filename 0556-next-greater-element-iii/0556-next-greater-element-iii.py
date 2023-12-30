class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = list(str(n)) 
        point  = len(a) - 2
        
        while point>=0 and a[point] >= a[point +1]:
            point -= 1
        if point == -1:
            return -1
        for i in range(len(a)-1,point,-1):
            if a[point] <a[i]:
                a[point],a[i] = a[i],a[point]
                break
        a[point + 1:] = sorted(a[point + 1:])
        result = int(''.join(a))
        if result >= 2 ** 31 or result <= n:
            return -1
    
        return result
                
        