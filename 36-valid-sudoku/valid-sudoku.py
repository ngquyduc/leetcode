from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def square(r, c):
            return r // 3 * 3 + c // 3
        hash_table = defaultdict(lambda: set())
        for m in range(len(board)):
            for n in range(len(board[0])):
                num = board[m][n]
                if num == ".":
                    continue
                r = "r" + str(m)
                c = "c" + str(n)
                s = "s" + str(square(m, n))
                if num in hash_table[r] or num in hash_table[c] or num in hash_table[s]:
                    return False
                hash_table[r].add(num)
                hash_table[c].add(num)
                hash_table[s].add(num)
        return True