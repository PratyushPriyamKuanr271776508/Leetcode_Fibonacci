typedef long long int ll;

#define pii pair<ll, ll>
#define F first
# define S second

const ll INF = 1e18;

class Solution {    
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int n = nums.size();
        
        vector<pii> val_and_cost;
        for (int j = 0; j < n; j ++) val_and_cost.push_back({nums[j], cost[j]});
        sort (val_and_cost.begin(), val_and_cost.end());
        
        vector<ll> prefix_cost(n);
        prefix_cost[0] = val_and_cost[0].S;
        for (int j = 1; j < n; j ++) prefix_cost[j] = prefix_cost[j-1] + val_and_cost[j].S;
        
        ll x = 1;
        ll costTillX = 0;
        for (int j = 0; j < n; j ++) costTillX += (ll)val_and_cost[j].S * abs(val_and_cost[j].F - x);
        
        ll result = INF;
        int index_till_less_x = 0;
        
        for (int target = x; target <= 1e6; target ++) {            
            result = min (result, costTillX);
            
            while (index_till_less_x < n && val_and_cost[index_till_less_x].F <= x) index_till_less_x ++;
            
            ll move_up_cost = (index_till_less_x > 0)? prefix_cost[index_till_less_x - 1] : 0;
            ll move_dwn_cost = prefix_cost [n-1] - move_up_cost;
        
            x ++;
            costTillX += move_up_cost - move_dwn_cost;
        }
        return result;
    }
};