class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        n, m = len(nums1), len(nums2)
        
        def dp(i, j):
            stNums1 = []
            stNums2 = []
            for x in range(n):
                while i!=0 and stNums1 and stNums1[-1] < nums1[x] and n - x >= i - len(stNums1) + 1: stNums1.pop()
                if len(stNums1) < i: stNums1.append(nums1[x])
            
            for x in range(m):
                while j!=0 and stNums2 and stNums2[-1] < nums2[x] and m - x >= j - len(stNums2) + 1: stNums2.pop()
                if len(stNums2) < j: stNums2.append(nums2[x])
            
            a, b = collections.deque(stNums1), collections.deque(stNums2)
                    
            ans = [max(a, b).popleft() for _ in a+b]
            
            return ans
                
    
        maxNum = []
        for i in range(n+1):
            if i < k and k - i > m: continue
            if i > k: continue
            maxNum = max(maxNum, dp(i, k - i), key= lambda x: "".join([str(h) for h in x]))
            
        return maxNum
            