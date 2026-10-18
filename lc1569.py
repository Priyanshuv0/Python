class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv[i - 1] = inv[i] * i % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            ways = fact[len(arr) - 1]
            ways = ways * inv[len(left)] % MOD
            ways = ways * inv[len(right)] % MOD

            return ways * dfs(left) * dfs(right) % MOD

        return (dfs(nums) - 1) % MOD
