class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        flag = False
        for c in s[::-1]:
            if c == " ":
                if flag:
                    return l
                continue
            else:
                l += 1
                flag = True
        return l