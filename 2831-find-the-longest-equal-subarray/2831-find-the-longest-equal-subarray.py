class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        
        def check(m):
            
            count = collections.Counter()
            i = 0
            maxVal = -1
            for j in range(N):
                count[nums[j]] += 1
                if count[nums[j]] > count[maxVal]: maxVal = nums[j]
                if (j - i + 1) - count[maxVal] <= k:
                    if count[maxVal] == m: return True
                else:
                    count[nums[i]] -= 1
                    i += 1
            return False
        
        l, r = 0, N
        
        while l < r:
            
            m = (l + r + 1) // 2
            if check(m):
                l = m
            else: r = m - 1
                
        return l
                

        