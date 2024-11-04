class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        last = word[0]
        res = ""
        for s in word[1:]:
            print(s)
            if last == s:
                if count == 9:
                    res += str(count)
                    res += s
                    count = 1
                else: 
                    count += 1
            else:
                res += str(count)
                res += last
                last = s
                count = 1
        res += str(count)
        res += last
        return res