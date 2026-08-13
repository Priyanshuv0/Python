class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        a = list(s)
        tree = [None] * (4 * n)

        def merge(x, y):
            if x is None:
                return y
            if y is None:
                return x

            lc, rc, pre, suf, best, ln = x
            lc2, rc2, pre2, suf2, best2, ln2 = y

            pre3 = pre
            if pre == ln and rc == lc2:
                pre3 = ln + pre2

            suf3 = suf2
            if suf2 == ln2 and rc == lc2:
                suf3 = ln2 + suf

            best3 = max(best, best2)
            if rc == lc2:
                best3 = max(best3, suf + pre2)

            return (lc, rc2, pre3, suf3, best3, ln + ln2)

        def build(v, l, r):
            if l == r:
                tree[v] = (a[l], a[l], 1, 1, 1, 1)
                return
            m = (l + r) // 2
            build(v * 2, l, m)
            build(v * 2 + 1, m + 1, r)
            tree[v] = merge(tree[v * 2], tree[v * 2 + 1])

        def update(v, l, r, p, c):
            if l == r:
                tree[v] = (c, c, 1, 1, 1, 1)
                return
            m = (l + r) // 2
            if p <= m:
                update(v * 2, l, m, p, c)
            else:
                update(v * 2 + 1, m + 1, r, p, c)
            tree[v] = merge(tree[v * 2], tree[v * 2 + 1])

        build(1, 0, n - 1)
        ans = []

        for c, i in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, i, c)
            ans.append(tree[1][4])

        return ans
