class Solution:
    def romanToInt(self, s: str) -> int:
        
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        pre=d[s[-1]]
        res=0
        for i in s[::-1]:
            
            if d[i] >= pre:
                res+=d[i]
            else:
                res-=d[i]
                
            pre=d[i]
            
        return res
        
        