class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        N = len(arr)
        l, r = 0, N-1
        while l < r:
            m = (l + r) >> 1
            if arr[m+1] <= arr[m]: r = m
            else: l = m + 1
        return l