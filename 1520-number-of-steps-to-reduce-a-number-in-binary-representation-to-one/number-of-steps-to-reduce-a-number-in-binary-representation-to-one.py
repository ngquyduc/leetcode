class Solution:
    def numSteps(self, s: str) -> int:
        r = 0
        while s != "1":
            if s[len(s) - 1] == '1':
                s = s[:-1] + '0'
                for c in range(len(s) - 2, -1, -1):
                    if s[c] == '1':
                        s = s[:c] + '0' + s[c + 1:]
                        if c == 0:
                            s = '1' + s
                    else:
                        s = s[:c] + '1' + s[c + 1:]
                        break
            else:
                s = s[:-1]
            r += 1
        return r
                   