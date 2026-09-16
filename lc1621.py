class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

        return dp[n + k - 1][k] if False else self.comb(n + k - 1, 2 * k)

    def comb(self, n, r):
        MOD = 10**9 + 7
        res = 1

        for i in range(1, r + 1):
            res = res * (n - r + i) % MOD
            res = res * pow(i, MOD - 2, MOD) % MOD

        return res
