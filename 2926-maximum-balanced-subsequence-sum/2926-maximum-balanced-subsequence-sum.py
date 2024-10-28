from sortedcontainers import SortedList
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        st = SortedList([(-inf, 0)])
        maxVal = -inf
        for i in range(n):
            if nums[i] > 0:
                idx = st.bisect_right((nums[i]-i, inf))
                s = st[idx-1][1] + nums[i]
                st.add((nums[i]-i, s))
                while idx + 1 < len(st) and st[idx + 1][1] < s: st.pop(idx + 1)
                maxVal = max(maxVal, s)
            maxVal = max(maxVal, nums[i])
        return maxVal