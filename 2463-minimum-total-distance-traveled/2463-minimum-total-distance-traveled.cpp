class Solution {
public:
    long long solve(int i, int j, int& n, int& m, vector<int>& robot, vector<vector<int>>& factory, vector<vector<vector<long long>>>& dp, int k) {
        if (i == n) {
            return 0;
        }
        if (j == m) {
            return 1e15;
        }
        if (dp[i][j][k] != -1) {
            return dp[i][j][k];
        }

        if(factory[j][1] > 0) {
            factory[j][1]--;
            dp[i][j][k] = abs(robot[i] - factory[j][0]) + solve(i+1,j,n,m,robot,factory,dp,k+1);
            factory[j][1]++;
            dp[i][j][k] = min(dp[i][j][k], solve(i,j+1,n,m,robot,factory,dp,0));
        }
        else {
            dp[i][j][k] = solve(i,j+1,n,m,robot,factory,dp,0);
        }
        return dp[i][j][k];
    }

    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        int n = robot.size(), m = factory.size();
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());


        vector<vector<vector<long long>>> dp(n, vector<vector<long long>>(m, vector<long long>(n, -1)));
        return solve(0, 0, n, m, robot, factory, dp, 0);
    }
};