class Solution:
    def maximumLengthSubstring(self, s):
        d = {}
        l = 0
        ans = 0

        for r, c in enumerate(s):
            d[c] = d.get(c, 0) + 1

            while d[c] > 2:
                d[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
