#define pii pair<int, int>
#define F first
#define S second

vector<pii> neigh = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

struct MyGrid {
    vector<vector<int>> grid;
    int rows, cols;
    queue<pii> fires;
    vector<vector<bool>> visited;
    
    MyGrid(const vector<vector<int>>& _grid) {
        grid = _grid;
        rows = grid.size();
        cols = grid[0].size();
        
        visited.resize(rows, vector<bool>(cols, false));
        for (int r = 0; r < rows; r ++) {
            for (int c = 0; c < cols; c ++) {
                if (grid[r][c] != 1) continue;
                
                visited[r][c] = true;
                fires.push({r, c});
            }
        }
    }
    
    void Spread() {
        queue<pii> new_fires;
    
        while (!fires.empty()) {
            pii cur = fires.front();
            fires.pop();
            
            for (auto i : neigh) {
                pii nxt = {cur.F+i.F, cur.S+i.S};
                
                bool valid = (nxt.F >= 0 && nxt.F < rows && nxt.S >= 0 && nxt.S < cols);
                if (!valid || visited[nxt.F][nxt.S] || grid[nxt.F][nxt.S] != 0) continue;
                
                new_fires.push(nxt);
                grid[nxt.F][nxt.S] = 1;
                visited[nxt.F][nxt.S] = true;
            }
        }
        
        fires = new_fires;
    }
};

class Solution {
    
    bool IsReachable (MyGrid& grid, int rows, int cols) {        
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        queue<pii> q;
        q.push({0, 0});
        visited[0][0] = true;
        
        while (!q.empty()) {
            queue<pii> new_q;
            
            while (!q.empty()) {
                pii cur = q.front();
                q.pop();
                if (grid.grid[cur.F][cur.S] != 0) continue;
                
                // cout << cur.F << " " << cur.S << endl;

                for (auto i : neigh) {
                    pii nxt = {cur.F+i.F, cur.S+i.S};

                    bool valid = (nxt.F >= 0 && nxt.F < rows && nxt.S >= 0 && nxt.S < cols);
                    if (!valid || visited[nxt.F][nxt.S] || grid.grid[nxt.F][nxt.S] != 0) continue;

                    new_q.push(nxt);
                    visited[nxt.F][nxt.S] = true;
                    if (nxt.F == rows-1 && nxt.S == cols-1) return true;
                }
            }
            
            grid.Spread();
            if (grid.grid[rows-1][cols-1] != 0) return false;
            q = new_q;
        }
        
        return false;
    }
    
    bool IsValid (int moves, const vector<vector<int>>& grid) {
        MyGrid new_grid (grid);
        
        for (int i = 0; i < moves; i ++) {
            if (new_grid.fires.empty()) break;
            new_grid.Spread();
        } 
        
        return IsReachable (new_grid, grid.size(), grid[0].size());
    }
    
public:
    int maximumMinutes(vector<vector<int>>& grid) {        
        int l = -1, r = 1e9;
        while (l < r) {
            int m = (l+r) >> 1;
            if (IsValid(m+1, grid)) l = m+1;
            else r = m;
        }
        // if (IsValid (l, grid)) return l;
        // return -1;
        return l;
    }
};