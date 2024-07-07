class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        N = len(buildings)
        Q = []
        for i in range(N): Q.extend([[buildings[i][0], -buildings[i][2]], [buildings[i][1], buildings[i][2]]])
        Q.sort()
        current, pending = [0], []
        prevMaxcurr = 0
        ans = []
        for i in range(2*N):
            if Q[i][1] < 0: 
                heapq.heappush(current, Q[i][1])
                if prevMaxcurr != current[0]: 
                    ans.append([Q[i][0], -Q[i][1]])
            else:
                heapq.heappush(pending, -Q[i][1])
                while current and pending and current[0] == pending[0]:
                    heapq.heappop(current)
                    heapq.heappop(pending)
                if prevMaxcurr != current[0]: 
                    ans.append([Q[i][0], -current[0]])
            prevMaxcurr = current[0]          
        return ans
                
                    
            
            
        