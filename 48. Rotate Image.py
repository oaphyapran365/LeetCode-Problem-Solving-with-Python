class Solution:
    def rotate(self, A):
        """
         Do not return anything, modify matrix in-place instead.
        """
        """
         [::-1] to flip the matrix upside down and then zip to transpose it. 
         It assigns the result back into A, so it's "in-place" in a sense
        """

        A[:] = zip(*A[::-1])