from collections import defaultdict, Counter

class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        if k == 1:
            cnt = Counter(nums)
            candidates = [x for x in cnt if cnt[x] == 1]
            return max(candidates) if candidates else -1
        candidate_indices = set(range(min(k - 1, n))) | set(range(max(0, n - k + 1), n))
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        ans = -1
        for i in candidate_indices:
            x = nums[i]
            total = 0
            cur_lo = cur_hi = None
            for j in pos[x]:
                lo = max(0, j - k + 1)
                hi = min(j, n - k)
                if cur_lo is None:
                    cur_lo, cur_hi = lo, hi
                elif lo <= cur_hi + 1:
                    cur_hi = max(cur_hi, hi)
                else:
                    total += cur_hi - cur_lo + 1
                    cur_lo, cur_hi = lo, hi
            if cur_lo is not None:
                total += cur_hi - cur_lo + 1
            if total == 1:
                ans = max(ans, x)
        return ans
