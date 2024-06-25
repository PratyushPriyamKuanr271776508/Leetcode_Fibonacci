import copy
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # Will calculate the heights row-wise and then column-wise
        V, H = copy.deepcopy(matrix), copy.deepcopy(matrix)
        for i in range(rows):
            for j in range(cols):
                if i > 0: V[i][j] = V[i-1][j] + 1 if matrix[i][j] == '1' else 0
                else: V[i][j] = int(matrix[i][j])
                if j > 0: H[i][j] = H[i][j-1] + 1 if matrix[i][j] == '1' else 0
                else: H[i][j] = int(matrix[i][j])
        
        maxArea = 0
        for i in range(rows):
            st = []
            for j in range(cols):
                while st and V[i][st[-1]] > V[i][j]:
                    Y = st.pop()
                    val = V[i][Y]
                    maxArea = max(maxArea, val * (j - st[-1] - 1) if st else val * (j - Y))
                st.append(j)
            while st:
                X = st.pop()
                maxArea = max(maxArea, V[i][X]*(cols - (st[-1] + 1 if st else 0)))
        
        for j in range(cols):
            st = []
            for i in range(rows):
                while st and H[st[-1]][j] > H[i][j]:
                    Y = st.pop()
                    val = H[Y][j]
                    maxArea = max(maxArea, val * (i - st[-1] - 1) if st else val * (i - Y))
                st.append(i)
            while st:
                X = st.pop()
                maxArea = max(maxArea, H[X][j]*(rows - (st[-1] + 1 if st else 0)))        
        
        return maxArea
        