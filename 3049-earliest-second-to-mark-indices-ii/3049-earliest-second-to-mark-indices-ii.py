from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    
    def __init__(self):
        self.n = 0
        self.arr = []
        self.ci = []
    
    def IsValid(self, till: int) -> bool:
        first_occur = [-1] * (self.n + 1)
        
        for j in range(till + 1):
            if first_occur[self.ci[j]] != -1:
                continue
            first_occur[self.ci[j]] = j
        
        extra = 0
        pq = SortedList()
        
        for t in range(till, -1, -1):
            if first_occur[self.ci[t]] != t:
                extra += 1
                continue
            
            val = self.arr[self.ci[t] - 1]
            if val == 0:
                extra += 1
                continue
            
            pq.add(val)
            if extra > 0:
                extra -= 1
            else:
                extra += 1
                pq.pop(0)
        
        pq_sum = sum(pq)
        arr_sum = sum(self.arr)
        
        req = arr_sum - pq_sum + self.n - len(pq)
        print(f"{till} {req} {extra}")
        
        return req <= extra
    
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        self.n = len(nums)
        self.ci = changeIndices
        self.arr = nums
        
        l, r = 0, len(self.ci) - 1
        while l < r:
            m = (l + r) // 2
            
            if self.IsValid(m):
                r = m
            else:
                l = m + 1
        
        return l + 1 if self.IsValid(l) else -1
