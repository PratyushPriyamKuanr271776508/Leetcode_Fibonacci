from typing import List

class Solution:
    def binary_search(self, nums: List[int], change_indices: List[int], idx: int) -> bool:
        last = {}
        for i in range(idx):
            last[change_indices[i]] = i
        
        if len(last) != len(nums):
            return False
        
        cnt = 0  # record how many numbers can be reduced
        for i in range(idx):
            # Check if this is the last occurrence of the index in change_indices
            if i == last[change_indices[i]]:
                if cnt < nums[change_indices[i] - 1]:
                    return False
                else:
                    cnt -= nums[change_indices[i] - 1]
            else:
                cnt += 1
        
        return True
    
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        l, r = 0, m + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.binary_search(nums, changeIndices, mid):
                r = mid
            else:
                l = mid + 1
        
        return -1 if r == m + 1 else r
