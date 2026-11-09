class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        import heapq

        free = list(range(k))
        heapq.heapify(free)

        busy = []
        count = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                heapq.heappush(free, server)

            if not free:
                continue

            idx = heapq.heappop(free)
            count[idx] += 1
            heapq.heappush(busy, (a + l, idx))

        mx = max(count)
        return [i for i in range(k) if count[i] == mx]
