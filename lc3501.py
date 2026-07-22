import itertools
from dataclasses import dataclass


@dataclass
class ZeroGroup:
    start: int
    length: int


class SparseTable:
    def __init__(self, values: list[int]):
        self.n = len(values)
        levels = self.n.bit_length() + 1
        self.table = [[0] * (self.n + 1) for _ in range(levels)]
        self.table[0] = values.copy()
        for level in range(1, levels):
            half = 1 << (level - 1)
            for j in range(self.n - (1 << level) + 1):
                self.table[level][j] = max(
                    self.table[level - 1][j],
                    self.table[level - 1][j + half]
                )

    def query_max(self, lo: int, hi: int) -> int:
        level = (hi - lo + 1).bit_length() - 1
        span = 1 << level
        return max(self.table[level][lo], self.table[level][hi - span + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        total_ones = s.count('1')

        zero_groups: list[ZeroGroup] = []
        group_of = [-1] * len(s)

        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1].length += 1
                else:
                    zero_groups.append(ZeroGroup(i, 1))
            group_of[i] = len(zero_groups) - 1

        if not zero_groups:
            return [total_ones] * len(queries)

        merge_lengths = [a.length + b.length for a, b in itertools.pairwise(zero_groups)]
        sparse = SparseTable(merge_lengths)

        def solve(l: int, r: int) -> int:
            gl = group_of[l]
            gr = group_of[r]

            left_tail = -1 if gl == -1 else zero_groups[gl].length - (l - zero_groups[gl].start)
            right_head = -1 if gr == -1 else r - zero_groups[gr].start + 1

            start_idx = gl + 1
            end_idx = gr if s[r] == '1' else gr - 1
            end_idx -= 1

            best = total_ones

            if s[l] == '0' and s[r] == '0' and gl + 1 == gr:
                best = max(best, total_ones + left_tail + right_head)
            elif start_idx <= end_idx:
                best = max(best, total_ones + sparse.query_max(start_idx, end_idx))

            inner_end = gr if s[r] == '1' else gr - 1
            if s[l] == '0' and gl + 1 <= inner_end:
                best = max(best, total_ones + left_tail + zero_groups[gl + 1].length)

            if s[r] == '0' and gl < gr - 1:
                best = max(best, total_ones + right_head + zero_groups[gr - 1].length)

            return best

        return [solve(l, r) for l, r in queries]
