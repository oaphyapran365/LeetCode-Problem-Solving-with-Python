class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            print(s)
            if s == '' :
                return True
        return False
        