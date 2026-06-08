class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = {}
        def dfs(x, y, cur_len):
            max_len = 0
            for dx, dy in dirs:
                if 0 <= dx + x < len(matrix) and 0 <= dy + y < len(matrix[0]) and (matrix[dx + x][dy + y] > matrix[x][y]):
                    if (dx + x, dy + y) in memo:
                        max_len = max(max_len, memo[(dx + x, dy + y)])
                    else:
                        max_len = max(dfs(dx + x, dy + y, cur_len + 1), max_len)
                    #print(f"{x} {y} x y || {dx + x} {dy + y} || {matrix[dx + x][dy + y]} {memo[(dx + x, dy + y)]}")
            
            memo[(x, y)] = max_len + 1
            return max_len + 1
        
        max_amt = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_amt = max(max_amt, dfs(i, j, 1))

        return max_amt
        