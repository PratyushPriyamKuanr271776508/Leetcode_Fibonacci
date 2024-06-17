class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0] * (k+1)
        m = [prices[0]] * (k+1)
        for i in range(1, n):
            for j in range(1, k+1):
                m[j] = min(m[j], prices[i] - dp[j-1])
                dp[j] = max(dp[j], prices[i]-m[j])
        return dp[k]