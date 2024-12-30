class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(0, numRows):
            level = []
            for j in range(0, i + 1):
                level.append(math.comb(i, j))
            result.append(level)
        return result
