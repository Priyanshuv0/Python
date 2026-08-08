class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suf = [n + 1] * (m + 1)
        suf[m] = n
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        result = []
        i = 0
        used = False
        for j in range(m):
            matched = False
            while i < n:
                if word1[i] == word2[j]:
                    result.append(i)
                    i += 1
                    matched = True
                    break
                elif not used and suf[j + 1] <= i + 1:
                    result.append(i)
                    i += 1
                    used = True
                    matched = True
                    break
                else:
                    i += 1
            if not matched:
                return []
        return result
