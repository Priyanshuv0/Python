class Solution:
    def stoneGameV(self, stoneValue) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == j:
                return 0
            best = 0
            for k in range(i, j):
                left = prefix[k + 1] - prefix[i]
                right = prefix[j + 1] - prefix[k + 1]
                if left < right:
                    best = max(best, left + dp(i, k))
                elif left > right:
                    best = max(best, right + dp(k + 1, j))
                else:
                    best = max(best, left + dp(i, k), right + dp(k + 1, j))
            return best

        result = dp(0, n - 1)
        dp.cache_clear()
        return result
