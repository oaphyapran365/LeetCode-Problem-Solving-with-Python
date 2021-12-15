#solved but Time Limit Exceeded

class Solution:
    def countPrimes(self, n: int) -> int:
        ctr = 0
        for num in range(n):
            if num <= 1:
                continue
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                 ctr += 1
                    
        return ctr
                        
        
        
                
        
        
        
		