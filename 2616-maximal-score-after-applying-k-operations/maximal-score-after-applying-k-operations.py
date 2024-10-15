import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        neg = [-n for n in nums]
        heapq.heapify(neg)
        res = 0
        for i in range(k):
            val = -heapq.heappop(neg)
            res += val
            heapq.heappush(neg, -math.ceil(val / 3))
        return res