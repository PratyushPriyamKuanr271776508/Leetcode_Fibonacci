class Solution:
    def solve(self, i, j, k, n, m, robot, factory, dp):

        if i == n:
            return 0
        if j == m:
            return 1e15
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        
        if factory[j][1] > 0:
            factory[j][1] -= 1
            dp[i][j][k] = abs(robot[i] - factory[j][0]) + self.solve(i + 1, j, k + 1, n, m, robot, factory, dp)
            factory[j][1] += 1
            dp[i][j][k] = min(dp[i][j][k], self.solve(i, j + 1, 0, n, m, robot, factory, dp))
        else:
            dp[i][j][k] = self.solve(i, j + 1, 0, n, m, robot, factory, dp)
        
        
        return dp[i][j][k]
    
    def minimumTotalDistance(self, robot, factory):
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()
        dp = [[[-1] * n for i in range(m)] for _ in range(n)]
        # self.solve(0, 0, n, m, 0, robot, factory, dp)
        # print(dp)
        return self.solve(0, 0, 0, n, m, robot, factory, dp)
