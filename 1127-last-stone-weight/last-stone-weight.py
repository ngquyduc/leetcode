class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = len(stones)
        for i in range(l):
            stones[i] = -stones[i]
        heap = stones
        heapq.heapify(heap)
        while l > 1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                z = y - x
                heapq.heappush(heap, z)
                l -= 1
            else:
                l -= 2
        return -heapq.heappop(heap) if len(heap) > 0 else 0
            