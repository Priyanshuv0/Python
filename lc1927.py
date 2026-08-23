class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_sum = right_sum = left_cnt = right_cnt = 0
        for i in range(n // 2):
            if num[i] == '?':
                left_cnt += 1
            else:
                left_sum += int(num[i])
        for i in range(n // 2, n):
            if num[i] == '?':
                right_cnt += 1
            else:
                right_sum += int(num[i])
        total_cnt = left_cnt + right_cnt
        if total_cnt % 2 == 1:
            return True
        diff = left_sum - right_sum
        return diff != (right_cnt - left_cnt) // 2 * 9
