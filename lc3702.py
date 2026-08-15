class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0
        z = 0

        for v in nums:
            x ^= v
            z += v == 0

        if x:
            return n

        return 0 if z == n else n - 1
