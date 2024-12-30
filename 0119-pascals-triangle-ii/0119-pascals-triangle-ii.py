class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(0, rowIndex + 1):
            result.append(math.comb(rowIndex, i))
        return result
        