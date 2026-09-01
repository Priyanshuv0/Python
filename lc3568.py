class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque

        m, n = len(classroom), len(classroom[0])
        d = [[-1] * n for _ in range(m)]
        x = y = cnt = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    x, y = i, j
                elif classroom[i][j] == 'L':
                    d[i][j] = cnt
                    cnt += 1

        if cnt == 0:
            return 0

        q = deque([(x, y, energy, 0, 0)])
        vis = {(x, y, energy, 0)}
        target = (1 << cnt) - 1

        while q:
            i, j, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if classroom[ni][nj] == 'X' or e == 0:
                    continue

                ne = e - 1
                nm = mask

                if classroom[ni][nj] == 'L':
                    nm |= 1 << d[ni][nj]

                if classroom[ni][nj] == 'R':
                    ne = energy

                state = (ni, nj, ne, nm)

                if state not in vis:
                    vis.add(state)
                    q.append((ni, nj, ne, nm, moves + 1))

        return -1
