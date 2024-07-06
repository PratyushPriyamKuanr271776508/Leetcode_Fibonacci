class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, float('inf')))
        prev = ans = 0
        for i in range(len(stations)):
            startFuel -= stations[i][0] - prev
            while pq and startFuel < 0:
                startFuel += -heapq.heappop(pq)
                ans += 1
            if startFuel < 0: return -1
            heapq.heappush(pq, -stations[i][1])
            prev = stations[i][0]
        return ans
                
        