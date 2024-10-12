class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        lo, hi = 0, max(nums)
        N = len(nums)
        
        def check(val, arr):
            
            for i in range(N-1):
                
                if arr[i] > val: return False
                arr[i+1] -= val - arr[i]
            if arr[N-1] > val: return False
            return True
        
        while lo < hi:
            
            mid = (lo + hi) >> 1
            if check(mid, nums[:]): hi = mid
            else: lo = mid + 1
        
        return lo
            
        