class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                v = res[i - 1][j] + res[i - 1][j - 1]
                temp.append(v)
            temp.append(1)
            res.append(temp)
        return res
