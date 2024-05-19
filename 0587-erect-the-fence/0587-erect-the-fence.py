from functools import cmp_to_key
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p1, p2, p3): return ((p2[0]-p1[0])*(p3[1]-p2[1]))-((p3[0]-p2[0])*(p2[1]-p1[1]))
        def distance(p1, p2): return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        def compare(p1, p2): 
            # p1 in consideration
            x = orientation(p0, p1, p2)
            if x > 0: return -1
            elif x < 0: return 1
            else: 
                if distance(p0, p1) > distance(p0, p2): return 1
                else: return -1
        
        n = len(trees)
        if n < 3: return trees
        bm = 0
        for i in range(1, n):
            y = trees[i][1]
            if y < trees[bm][1] or (y == trees[bm][1] and trees[i][0] < trees[bm][0]): bm = i
        trees[0], trees[bm] = trees[bm], trees[0]
        global p0
        p0 = trees[0]
        trees[1:] = sorted(trees[1:], key=cmp_to_key(compare))
        print(trees)
        st = [0, 1]
        xtra = []
        for i in range(2, n):
            while len(st) >= 2 and (orientation(trees[st[-2]], trees[st[-1]], trees[i])) < 0:  st.pop()
            st.append(i)
        ans = []
        for i in range(1, len(trees)):
            if i != st[-1] and orientation(trees[0], trees[i], trees[st[-1]]) == 0: ans.append(tuple(trees[i]))
        for i in st: ans.append(tuple(trees[i]))
        return set(ans)
        
        
        