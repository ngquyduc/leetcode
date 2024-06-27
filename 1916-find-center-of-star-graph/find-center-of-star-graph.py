class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()
        for [v1, v2] in edges:
            if v1 in visited:
                return v1
            if v2 in visited:
                return v2
            visited.update([v1, v2])