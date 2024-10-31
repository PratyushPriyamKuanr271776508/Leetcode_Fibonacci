class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        ps = [0]
        for i in nums: ps.append(ps[-1] + i)
            
        def cost(i, j, mid):
            c1 = nums[mid] * (mid - i + 1) - (ps[mid + 1] - ps[i])
            c2 = (ps[j + 1] - ps[mid]) - nums[mid] * (j - mid + 1)
            return c1 + c2
        
        def check(m):
            ans = inf
            for i in range(N - m + 1):
                c1 = cost(i, i + m - 1, (2*i + m - 1) // 2)
                if m % 2 == 0:
                    c2 = cost(i, i + m - 1, (2*i + m - 1) // 2 + 1)
                    ans = min(ans, c1, c2)
                else: ans = min(ans, c1)
            return ans <= k
        
        lo, hi = 0, N
        while lo < hi:
            m = (lo + hi + 1) >> 1
            if check(m): lo = m
            else: hi = m - 1
        return lo