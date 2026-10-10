class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        import heapq

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        heap = [-d for d in diff]
        heapq.heapify(heap)

        while k > 0 and heap and heap[0] < 0:
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -(largest - 1))
            k -= 1

        return sum(d * d for d in [-x for x in heap])
