class Solution:
    def maximumWeight(self, intervals):
        from bisect import bisect_left

        a = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(a)
        ends = [x[0] for x in a]

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for i in range(1, n + 1):
            r, l, w, idx = a[i - 1]
            p = bisect_left(ends, l, 0, i - 1)

            for k in range(1, 5):
                w1, s1 = dp[k][i - 1]
                w2, s2 = dp[k - 1][p]
                s2 = tuple(sorted(s2 + (idx,)))
                w2 += w

                if w2 > w1 or (w2 == w1 and s2 < s1):
                    dp[k][i] = (w2, s2)
                else:
                    dp[k][i] = dp[k][i - 1]

        return list(dp[4][n][1])
