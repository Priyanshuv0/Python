class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in order]
        pos_of = [0] * n
        for idx, orig in enumerate(order):
            pos_of[orig] = idx

        R = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and sorted_vals[j + 1] - sorted_vals[i] <= maxDiff:
                j += 1
            R[i] = j

        LOG = max(1, n.bit_length() + 1)
        up = [[0] * n for _ in range(LOG)]
        up[0] = R[:]
        for k in range(1, LOG):
            prev = up[k - 1]
            for i in range(n):
                up[k][i] = prev[prev[i]]

        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue

            p, q = pos_of[u], pos_of[v]
            if p > q:
                p, q = q, p

            cur = p
            dist = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < q:
                    cur = up[k][cur]
                    dist += (1 << k)

            if cur >= q:
                answer.append(dist)
            elif up[0][cur] >= q:
                answer.append(dist + 1)
            else:
                answer.append(-1)

        return answer
