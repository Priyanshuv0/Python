class Solution:
    def maxSubarrayLength(self, nums, k):
        from collections import defaultdict

        d = defaultdict(int)
        l = 0
        ans = 0

        for r, x in enumerate(nums):
            d[x] += 1

            while d[x] > k:
                d[nums[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
