class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        a = sorted((x, i) for i, x in enumerate(nums))
        ans = [0] * len(nums)
        i = 0

        while i < len(nums):
            j = i
            while j + 1 < len(nums) and a[j + 1][0] - a[j][0] <= limit:
                j += 1

            vals = sorted(x for x, _ in a[i:j + 1])
            idx = sorted(k for _, k in a[i:j + 1])

            for k, v in zip(idx, vals):
                ans[k] = v

            i = j + 1

        return ans
