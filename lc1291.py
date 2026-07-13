class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        digits = "123456789"
        result = []

        for length in range(1, 10):
            for start in range(0, 10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)

        result.sort()
        return result
