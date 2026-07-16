from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(gcd(num, mx))

        prefix_gcd.sort()

        total = 0
        left, right = 0, n - 1

        while left < right:
            total += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return total
