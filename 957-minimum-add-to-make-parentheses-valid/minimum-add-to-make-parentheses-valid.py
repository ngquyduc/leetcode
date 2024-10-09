class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = {"(": ")"}
        stack = list()
        for c in s:
            if len(stack) != 0 and c == need.get(stack[-1]):
                stack.pop(-1)
            else:
                stack.append(c)
        return len(stack)
