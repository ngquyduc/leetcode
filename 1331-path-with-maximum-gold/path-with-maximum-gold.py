class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        res = 0

        def dfs(grid, m, n, r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0:
                return 0
            res = 0
            val = grid[r][c]
            grid[r][c] = 0
            for d in range(4):
                res = max(res, dfs(grid, m, n, r + dirs[d][0], c + dirs[d][1]))
            grid[r][c] = val
            return res + val
            
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(grid, m, n, r, c))
        return res