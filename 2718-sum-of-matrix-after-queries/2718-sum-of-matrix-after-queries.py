from typing import List, Tuple

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = [(-1, 0)] * n
        cols = [(-1, 0)] * n
        
        for j, q in enumerate(queries):
            if q[0] == 0:
                rows[q[1]] = (j, q[2])
            else:
                cols[q[1]] = (j, q[2])
        
        result = 0
        
        # Sorting columns based on the query index and value
        cols.sort()

        # Compute the prefix sums of column values
        prefix_cols = [0] * (n + 1)
        for j in range(1, n + 1):
            prefix_cols[j] = prefix_cols[j - 1] + cols[j - 1][1]

        # Process rows and sum the values
        for r in range(n):
            row = rows[r]
            col_pos = self.lower_bound(cols, row)

            result += col_pos * row[1]
            if col_pos < n:
                result += (prefix_cols[n] - prefix_cols[col_pos])
        
        return result

    # Helper function to implement lower_bound behavior
    def lower_bound(self, arr: List[Tuple[int, int]], target: Tuple[int, int]) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
