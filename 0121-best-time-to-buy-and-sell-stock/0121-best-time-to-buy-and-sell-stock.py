class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        st = []
        n = len(prices)
        overallP = 0
        localP = 0
        for i in range(n - 1, -1, -1):
            while st and prices[st[-1]] > prices[i]:
                localP = max(localP, prices[st.pop()])
            st.append(i)
            overallP = max(localP - prices[i], overallP)
        return overallP