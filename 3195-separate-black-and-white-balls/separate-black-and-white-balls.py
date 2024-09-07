class Solution:
    def minimumSteps(self, s: str) -> int:
        res, r = 0, len(s) - 1
        for i in range(len(s)):
            if i > r:
                break
            if s[i] == '1':
                while r > 0 and s[r] != '0':
                    r -= 1
                if i > r:
                    break
                res += r - i
                r -= 1
        return res
