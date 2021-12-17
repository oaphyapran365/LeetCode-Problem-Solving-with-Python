# Simple solution using Exponents and Log : faster then 92%
# faster than 20.43% of Python3 online submissions 

# Step 1:
# The logic is simple first we use the Exponent Rule of Multiplication which states:



# Lets call the two numbers we need to add num1 and num2.
# Therefore as long as we use the same base, we can raise that common base to num1 and num2 and multiply them.
# In this code I have chosen the common base of 2 but you can choose any number.

#       2 num1 x 2 num2 = 2 num1 + num2

# Lets call this result product.

# Step 2:
# Next we use the Log of Exponent Rule (Logarithm of a Base to a Power Rule), which states
#       loga(an ) = n

# In our case we take log base 2 of product which gives us the sum of num1 and num2 .

#       log2(2 (num1 + num2) ) = num1 + num2

# And that is the final answer.


import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        #raises 2 to the power a
        fact1=math.pow(2,a)
        #raises 2 to the power b
        fact2=math.pow(2,b)
        #by multiplying the 2 factors, the powers gets added
        #ie, 2^(a+b)
        prod=fact1*fact2
        """
         here we use the Log of Exponent Rule 
            -> log2(2^(a+b)) = a+b
         """
        ans=math.log2(prod)
        return int(ans)   