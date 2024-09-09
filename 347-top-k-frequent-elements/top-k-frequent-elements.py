from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, ht = set(), defaultdict(lambda: 0)
        for n in nums:
            ht[n] += 1
        ht = sorted(ht.items(), key=lambda x: -x[1])
        return list(map(lambda x: x[0], ht))[:k]
            