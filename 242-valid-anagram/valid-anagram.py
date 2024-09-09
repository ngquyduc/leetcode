from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht = defaultdict(lambda: 0)
        for c in s:
            ht[c] += 1
        for c in t:
            if ht[c] == 0:
                return False
            else:
                ht[c] -= 1
        return True