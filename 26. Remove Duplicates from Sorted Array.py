
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
	    duplicates = 0

	    for i in range(1, len(nums)):
		    if nums[i] == nums[i - 1]:
			    duplicates += 1
		    else:
			    nums[i - duplicates] = nums[i]

	    return (len(nums) - duplicates)