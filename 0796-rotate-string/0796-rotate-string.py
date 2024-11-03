class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal): return False
        s += s
        
        prevlps, i = -1, 1
        lps = [-1] * len(goal)
        
        while i < len(goal):
            if s[i] == s[prevlps + 1]:
                lps[i] = prevlps + 1
                prevlps += 1
                i += 1
            elif prevlps == -1:
                lps[i] == -1
                i += 1
            else:
                prevlps = lps[prevlps]
                
        i, j = 0, -1
        while i < len(s):
            if s[i] == goal[j + 1]:
                i += 1
                j += 1
            else:
                if j == -1:
                    i += 1
                else:
                    j = lps[j]
            if j == len(goal) - 1: return True
        return False