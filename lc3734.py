class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        mid = ""
        for i in range(26):
            if cnt[i] % 2:
                if mid:
                    return ""
                mid = chr(i + 97)
            cnt[i] //= 2

        n = len(s)
        m = n // 2
        left = []

        def possible():
            x = left[:]
            for i in range(25, -1, -1):
                x += [chr(i + 97)] * cnt[i]
            p = ''.join(x)
            return p + mid + p[::-1] > target

        for _ in range(m):
            ok = False
            for i in range(26):
                if cnt[i]:
                    cnt[i] -= 1
                    left.append(chr(i + 97))

                    if possible():
                        ok = True
                        break

                    left.pop()
                    cnt[i] += 1

            if not ok:
                return ""

        p = ''.join(left)
        ans = p + mid + p[::-1]

        return ans if ans > target else ""
