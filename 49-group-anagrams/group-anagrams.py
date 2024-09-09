from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(lambda: [])
        for s in strs:
            r = "".join(sorted(s))
            temp[r].append(s)
        return list(temp.values())
        