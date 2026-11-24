class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            p = 1
            for j in range(i, len(nums)):
                p *= nums[j]
                g = 0
                l = 1
                for k in range(i, j + 1):
                    g = gcd(g, nums[k])
                    l = l * nums[k] // gcd(l, nums[k])
                if p == g * l:
                    ans = max(ans, j - i + 1)
        return ans
