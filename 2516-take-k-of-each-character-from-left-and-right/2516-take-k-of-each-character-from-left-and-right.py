from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        """
        s = "aabaaaacaabc"
        k = 2
        
        we will have a left pointer and we will have a right pointer such that
        left <= right 
        
        and we have to maximize this window such that the number of each character outside the window satisfy the condition og at least k characters
        
        """
        N = len(s)
        total = Counter(s)
        
        # since k is the least value a character can occur outside the window we can have atmost total[char] - k characters
        # within the window
        
        withinTheWindow = {c: total[c] - k for c in 'abc'}
        if any(x < 0 for x in withinTheWindow.values()): return -1
        def check(mid):
            
            initialCount = Counter(s[:mid])
            if all(initialCount[ch] <= withinTheWindow[ch] for ch in 'abc'): return True     
            i = 1
            j = i + mid - 1
            
            while j < N:
                initialCount[s[j]] += 1
                initialCount[s[i-1]] -= 1
                if all(initialCount[ch] <= withinTheWindow[ch] for ch in 'abc'): return True    
                j += 1
                i += 1
                
            return False
        
        l = 0
        r = N
        
        while l < r:
            m = (l + r + 1) >> 1
            if check(m): 
                l = m
            else: r = m - 1
        
        return N-l
        