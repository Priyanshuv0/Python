class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        m = len(s)

        prefix_val = [0] * (m + 1)
        prefix_cnt = [0] * (m + 1)
        prefix_sum = [0] * (m + 1)

        for i in range(1, m + 1):
            d = int(s[i - 1])
            if d != 0:
                prefix_val[i] = (prefix_val[i - 1] * 10 + d) % MOD
                prefix_cnt[i] = prefix_cnt[i - 1] + 1
                prefix_sum[i] = prefix_sum[i - 1] + d
            else:
                prefix_val[i] = prefix_val[i - 1]
                prefix_cnt[i] = prefix_cnt[i - 1]
                prefix_sum[i] = prefix_sum[i - 1]

        max_cnt = m + 1
        pow10 = [1] * (max_cnt + 1)
        for i in range(1, max_cnt + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        answers = []

        for l, r in queries:
            left = prefix_val[l]
            right = prefix_val[r + 1]
            cnt_diff = prefix_cnt[r + 1] - prefix_cnt[l]

            x = (right - left * pow10[cnt_diff]) % MOD

            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            ans = (x * digit_sum) % MOD
            answers.append(ans)

        return answers
