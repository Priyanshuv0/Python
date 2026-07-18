from math import gcd
from functools import reduce

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return gcd(max(nums), min(nums))
