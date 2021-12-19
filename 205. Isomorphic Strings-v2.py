#Faster and space efficient
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = set(zip(s, t))
        return len(d) == len(set(s)) == len(set(t))