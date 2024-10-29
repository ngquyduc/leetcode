class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = dict()
        res = 0
        def dp(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            temp = 0
            for x, y in [(r-1, c+1), (r, c+1), (r+1, c+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[r][c]:
                    temp = max(temp, 1 + dp(x, y))
            memo[(r, c)] = temp
            return temp

        for r in range(m):
            res = max(res, dp(r, 0))

        return res