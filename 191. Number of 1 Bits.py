"""
Solution 1

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


"""

# Solution 2

class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for bit in str(bin(n)):
            if bit == '1':
                total += 1
                
        return total
                