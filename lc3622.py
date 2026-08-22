class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        x = n
        while x:
            x, d = divmod(x, 10)
            s += d
            p *= d
        return n % (s + p) == 0
