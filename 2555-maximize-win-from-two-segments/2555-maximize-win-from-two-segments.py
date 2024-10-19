class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        
        n = len(prizePositions)
    
        # Function to check if it's possible to collect at least `x` prizes using two segments
        def canCollectAtLeast(x):
            left = 0
            max_single_segment = [0] * n
            prizes_in_window = 0

            # First sliding window: Calculate the maximum number of prizes for one segment
            for right in range(n):
                while prizePositions[right] - prizePositions[left] > k:
                    left += 1
                prizes_in_window = right - left + 1
                if right > 0:
                    max_single_segment[right] = max(max_single_segment[right - 1], prizes_in_window)
                else:
                    max_single_segment[right] = prizes_in_window

                # Check if the first segment alone is enough
                if prizes_in_window >= x:
                    return True

            # Second sliding window: Combine two segments
            left = 0
            for right in range(n):
                while prizePositions[right] - prizePositions[left] > k:
                    left += 1
                prizes_in_window = right - left + 1

                # Try to combine this segment with a previous segment
                if left > 0 and prizes_in_window + max_single_segment[left - 1] >= x:
                    return True

            return False

        # Binary search for the maximum number of prizes that can be collected
        low, high = 0, n
        while low < high:
            mid = (low + high + 1) // 2  # Middle point of the binary search
            if canCollectAtLeast(mid):
                low = mid  # If we can collect at least `mid` prizes, search the higher range
            else:
                high = mid - 1  # Otherwise, search the lower range

        return low
                    
            
        