class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        curr = res = prev = 0
        curr_ops = "+"

        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1

                i -= 1
                match curr_ops:
                    case "+":
                        res += curr
                        prev = curr
                    case "-":
                        res -= curr
                        prev = -curr
                    case "*":
                        res -= prev
                        res += prev * curr
                        prev = prev * curr
                    case "/":
                        res -= prev
                        res += int(prev / curr)
                        prev = int(prev / curr)

                curr = 0

            elif s[i] != " ":
                curr_ops = s[i]

            i += 1

        return res
