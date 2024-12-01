class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        count2 = [0] * 26
        count1 = [[0] * 26 for _ in range(n + 1)]
        
        # Precompute character frequencies for `word2`
        for char in word2:
            count2[ord(char) - ord('a')] += 1
        
        # Precompute prefix character counts for `word1`
        for i in range(1, n + 1):
            char_idx = ord(word1[i - 1]) - ord('a')
            for j in range(26):
                count1[i][j] = count1[i - 1][j]
            count1[i][char_idx] += 1

        def is_valid(start, end):
            for i in range(26):
                if count1[end][i] - count1[start - 1][i] < count2[i]:
                    return False
            return True

        # Binary search to find the minimum valid right endpoint
        def binary_search(start):
            left, right = start, n + 1
            while left < right:
                mid = (left + right) // 2
                if is_valid(start, mid):
                    right = mid
                else:
                    left = mid + 1
            return left

        # Count valid substrings
        ans = 0
        for start in range(1, n + 1):
            right = binary_search(start)
            ans += n - right + 1
        
        return ans
