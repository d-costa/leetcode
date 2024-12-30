class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.comb(rowIndex, i) for i in range(0, rowIndex + 1)]
        