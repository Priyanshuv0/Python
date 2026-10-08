class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0

        for c in s:
            if c == '(':
                if balance > 0:
                    res.append(c)
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    res.append(c)

        return ''.join(res)
