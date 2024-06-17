import pprint
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ps = [0] 
        for i in range(n): ps.append(ps[-1]+nums[i])
        ans = [[""] * 4 for _ in range(n)]
        dp = [[0] * 4 for _ in range(n)]
        for i in range(n):
            for l in range(1, 4):
                a, b = dp[i-1][l], ps[i+1] - ps[i+1-k] + (0 if l == 1 else dp[i - k][l - 1])
                dp[i][l] = max(a, b)
                if a >= b: ans[i][l] = ans[i-1][l]
                else: ans[i][l] = ans[i - k][l - 1] +f" {i-k+1}"
#         print(dp[n-1][3])
        
#         pprint.pprint(dp)
#         pprint.pprint(ans)
        
        return [int(i) for i in ans[-1][-1].split(" ")[1:]]
                
        