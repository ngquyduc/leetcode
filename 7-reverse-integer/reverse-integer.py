class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        while x > 0:
            i = x % 10
            x = x // 10
            res = res * 10 + i
        if res > pow(2, 31) - 1 or res < pow(-2, 31):
            return 0
        return res if not flag else -res