class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2) #nums1 becomes [1,2,3,0,0,0,2,5,6]
        nums1.sort()       #nums1 becomes [0,0,0,1,2,2,3,5,6]
        for i in range(n):
            nums1.remove(0) #Remove n number of zeroes from the list from nums1 gives the required solution