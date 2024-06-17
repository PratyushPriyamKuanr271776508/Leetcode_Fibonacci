class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0] * 3
        m = [prices[0]] * 3
        for i in range(1, n):
            for k in range(1, 3):
                m[k] = min(m[k], prices[i] - dp[k-1])
                dp[k] = max(dp[k], prices[i]-m[k])
        return dp[2]