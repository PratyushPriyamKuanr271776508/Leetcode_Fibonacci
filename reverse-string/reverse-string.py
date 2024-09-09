class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)

        def recurse(i=0):
            if i >= N//2: return
            s[i], s[-i-1] = s[-i-1], s[i]
            recurse(i + 1)
        
        recurse()
        
        