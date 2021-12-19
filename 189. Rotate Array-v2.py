#Time Limit Exceeded
class Solution:
    def rotate(self, nums, k):
        
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            previous = nums[-1] #initiate a first previous 
            for i in range(len(nums)):
                temp = nums[i] #hodl nums[i]
                nums[i] = previous #overwrite the current index 
                previous = temp #swap the value 