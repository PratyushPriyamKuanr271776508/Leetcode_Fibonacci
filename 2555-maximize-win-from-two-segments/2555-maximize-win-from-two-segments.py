class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        
        n = len(prizePositions)

        # First sliding window to calculate max prizes for one segment
        left = 0
        prizes_in_window = 0
        max_single_segment = [0] * n

        for right in range(n):
            # Slide the window: all prize positions in the range [prizePositions[left], prizePositions[right]]
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            prizes_in_window = right - left + 1
            if right > 0:
                max_single_segment[right] = max(max_single_segment[right - 1], prizes_in_window)
            else:
                max_single_segment[right] = prizes_in_window

        # Second sliding window to check for maximum prizes with two segments
        result = max_single_segment[n - 1]  # Initialize result with max single segment value
        left = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            prizes_in_window = right - left + 1

            # Combine current window with the best non-overlapping window on the left
            if left > 0:
                result = max(result, prizes_in_window + max_single_segment[left - 1])
            else:
                result = max(result, prizes_in_window)

        return result
                    
            
        