class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        firstMissingPositive = 1
        
        for i in nums:
            if i == firstMissingPositive:
                firstMissingPositive += 1
                
        return firstMissingPositive
            
        