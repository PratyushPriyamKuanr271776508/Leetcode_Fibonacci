class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        Q = collections.deque([])
        N = len(points)
        lst = [(p[1] - p[0], p[0]) for p in points]
        Q = collections.deque([])
        ans = float('-inf')
        for i in range(N):
            while Q and lst[i][1] - Q[0][1] > k: Q.popleft()
            if Q: ans = max(ans, lst[i][0] + 2 * lst[i][1] + Q[0][0])
            while Q and Q[-1][0] < lst[i][0]: Q.pop()
            Q.append(lst[i])  
        return ans
        