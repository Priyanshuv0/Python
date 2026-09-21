class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            rem = num % k
            new_dp[rem] = 1

            for prev_rem in range(k):
                if dp[prev_rem] > 0:
                    new_dp[(prev_rem * rem) % k] += dp[prev_rem]

            for i in range(k):
                ans[i] += new_dp[i]

            dp = new_dp

        return ans
