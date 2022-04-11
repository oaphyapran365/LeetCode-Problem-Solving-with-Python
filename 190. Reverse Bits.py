'''
Convert 32 bit binary to a decimal in python

a = '00011110001101110110110000001000'
a_dec = int(a, 2)
print(a_dec)
'''



class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert int into 32 bit and reverse it. Convert 32 bit into int.
        a= '{0:032b}'.format(n)
        reverse = a[::-1]
        return int(reverse,2)
        