class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        x = len(nums)//2
        return nums[x]