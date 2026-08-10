class Solution:
    def getResults(self, queries):
        from sortedcontainers import SortedList

        n = max(q[1] for q in queries) + 1
        s = SortedList([0, n])
        t = [0] * (4 * (n + 1))

        def update(v, l, r, p, x):
            if l == r:
                t[v] = x
                return
            m = (l + r) // 2
            if p <= m:
                update(v * 2, l, m, p, x)
            else:
                update(v * 2 + 1, m + 1, r, p, x)
            t[v] = max(t[v * 2], t[v * 2 + 1])

        def query(v, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return t[v]
            m = (l + r) // 2
            return max(
                query(v * 2, l, m, ql, qr),
                query(v * 2 + 1, m + 1, r, ql, qr)
            )

        for i in range(1, len(s)):
            update(1, 0, n, s[i], s[i] - s[i - 1])

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = s.bisect_left(x)
                a, b = s[i - 1], s[i]
                s.add(x)
                update(1, 0, n, x, x - a)
                update(1, 0, n, b, b - x)
            else:
                x, k = q[1], q[2]
                i = s.bisect_right(x)
                a = s[i - 1]
                ans.append(max(
                    x - a,
                    query(1, 0, n, 0, x)
                ) >= k)

        return ans
