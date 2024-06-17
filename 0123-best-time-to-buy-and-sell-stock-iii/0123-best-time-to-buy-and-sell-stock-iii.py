class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [[0, 0, 0] for _ in range(n)]
        m = [prices[0]] * 3
        for i in range(1, n):
            for k in range(1, 3):
                m[k] = min(m[k], prices[i] - dp[i-1][k-1])
                dp[i][k] = max(dp[i-1][k], prices[i]-m[k])
        return dp[n-1][2]