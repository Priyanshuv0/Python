from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        s = list(accumulate(piles, initial=0))

        @cache
        def dfs(i, m):
            if 2 * m >= n - i:
                return s[n] - s[i]
            return max(
                s[n] - s[i] - dfs(i + x, max(m, x))
                for x in range(1, 2 * m + 1)
            )

        return dfs(0, 1)
