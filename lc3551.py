class Solution:
    def countPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (j - i) <= 2:
                    ans += 1

        return ans
