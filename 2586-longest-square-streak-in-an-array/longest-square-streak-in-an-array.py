from collections import defaultdict
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        set_nums = set(nums)
        hash_table = defaultdict(lambda: 1)
        res = 1
        for n in nums:
            if sqrt(n) in set_nums:
                hash_table[n] = hash_table[sqrt(n)] + 1
                res = max(res, hash_table[n])
        return res if res >= 2 else -1
        