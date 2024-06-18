from collections import defaultdict
class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        hash_map = defaultdict(lambda: 0)
        for i in range(len(difficulty)):
            if profit[i] > hash_map[difficulty[i]]:
                hash_map[difficulty[i]] = profit[i]
        len_dif = len(difficulty)
        difficulty.sort()
        worker.sort()
        highest_profit, lowest_difficulty_ptr, res = 0, 0, 0
        for w in worker:
            while lowest_difficulty_ptr < len_dif and w >= difficulty[lowest_difficulty_ptr]:
                highest_profit = max(
                    highest_profit, hash_map[difficulty[lowest_difficulty_ptr]]
                )
                lowest_difficulty_ptr += 1
            res += highest_profit
        return res