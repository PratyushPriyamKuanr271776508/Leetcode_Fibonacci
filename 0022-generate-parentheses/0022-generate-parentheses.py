class Solution(object):
    def generateParenthesis(self, n):
        
        dp = collections.defaultdict(list)
        dp[(0, 0)] = [""]
        
        for left in range(1, n+1):
            for right in range(left + 1):
                if left > right: dp[(left, right)] += [i + "(" for i in dp[(left-1, right)]]
                if right > 0: dp[(left, right)] += [i + ")" for i in dp[(left, right-1)]]
        return dp[(n, n)]
        
#         def recurse(left = 0, right = 0, ls = [], s = ""):
#             if left == right == n:
#                 ls.append(s)
#                 return
            
#             if left < n: recurse(left + 1, right, ls, s + '(')
#             if right < left: recurse(left, right + 1, ls, s + ')')
            
#             return ls
        # return recurse()



