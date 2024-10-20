class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_with_capability(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2  # Skip the next house to avoid robbing adjacent ones
                else:
                    i += 1
            return count >= k

        # Binary search to minimize the maximum capability
        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if can_rob_with_capability(mid):
                high = mid  # Try for a smaller capability
            else:
                low = mid + 1  # Increase the capability since it's not enough

        return low
        