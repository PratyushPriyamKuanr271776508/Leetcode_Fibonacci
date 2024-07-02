class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i,c in enumerate(s):
            if c=='*':
                heappop(heap)
            else:
                heappush(heap,(c,-i))
        
        ans = ['']*len(s)
        while heap:
            char,i = heappop(heap)
            ans[-i] = char
            
        return ''.join(ans)
            