class Solution(object):
    def generateParenthesis(self, n):
        
        def recurse(left = 0, right = 0, ls = [], s = ""):
            if left == right == n:
                ls.append(s)
                return
            
            if left < n: recurse(left + 1, right, ls, s + '(')
            if right < left: recurse(left, right + 1, ls, s + ')')
            
            return ls
        return recurse()



