class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        molqaviren = grid
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = {grid[i][j]}
                    continue

                curr = set()

                if i > 0:
                    curr.update(x ^ grid[i][j] for x in dp[j])

                if j > 0:
                    curr.update(x ^ grid[i][j] for x in dp[j - 1])

                dp[j] = curr

        return min(dp[-1])
