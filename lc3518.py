from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        half = [c // 2 for c in cnt]
        n_half = sum(half)
        odd_char = -1
        for i in range(26):
            if cnt[i] % 2 == 1:
                odd_char = i

        CAP = 2 * 10**6

        def count_perms(counts, total):
            if total == 0:
                return 1
            result = 1
            remaining = total
            for c in counts:
                if c == 0:
                    continue
                result *= comb(remaining, c)
                if result > CAP:
                    return CAP + 1
                remaining -= c
            return result

        if count_perms(half, n_half) < k:
            return ""

        half_str = []
        remaining_half = half[:]
        remaining_total = n_half
        for _ in range(n_half):
            placed = False
            for c in range(26):
                if remaining_half[c] == 0:
                    continue
                remaining_half[c] -= 1
                p = count_perms(remaining_half, remaining_total - 1)
                if p >= k:
                    half_str.append(chr(97 + c))
                    remaining_total -= 1
                    placed = True
                    break
                else:
                    k -= p
                    remaining_half[c] += 1
            if not placed:
                return ""

        half_s = "".join(half_str)
        mid = chr(97 + odd_char) if odd_char != -1 else ""
        return half_s + mid + half_s[::-1]
