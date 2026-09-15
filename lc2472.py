class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        pal = [[False] * n for _ in range(n)]

        for r in range(n):
            dp[r + 1] = dp[r]

            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True
                    if r - l + 1 >= k:
                        dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]
