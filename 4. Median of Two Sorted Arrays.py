class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        
        if n % 2 == 0:
            left = n // 2
            right = left + 1
            median = (arr[left-1] + arr[right-1]) / 2
        else:
            m = (n+1) //2
            median = arr[m - 1]
            
        return median
            