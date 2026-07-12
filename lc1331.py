class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique = sorted(set(arr))
        rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
        return [rank[x] for x in arr]
