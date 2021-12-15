class Solution:
    def isHappy(self, n):
        D = []
        while True:
            n = sum( int(x)**2 for x in str(n) )
            if n==1:
                return True
            elif n in D:
                return False
            else:
                D.append(n)