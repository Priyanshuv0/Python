from math import gcd
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1

        divisible_count = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            total = 0
            for multiple in range(d, max_val + 1, d):
                total += cnt[multiple]
            divisible_count[d] = total * (total - 1) // 2

        exact_count = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total = divisible_count[d]
            multiple = 2 * d
            while multiple <= max_val:
                total -= exact_count[multiple]
                multiple += d
            exact_count[d] = total

        prefix = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            prefix[d] = prefix[d - 1] + exact_count[d]

        answer = []
        for q in queries:
            target = q + 1
            d = bisect_right(prefix, target - 1)
            answer.append(d + 1 if prefix[d] < target else d)

        result = []
        for q in queries:
            target = q + 1
            lo, hi = 1, max_val
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            result.append(lo)

        return result
