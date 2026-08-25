class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for j in range(1, n - 1):
            l = min(nums[:j])
            r = min(nums[j + 1:])
            if l < nums[j] and r < nums[j]:
                ans = min(ans, l + nums[j] + r)
        return -1 if ans == float('inf') else ans
