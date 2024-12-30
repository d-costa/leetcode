class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for curr in range(0, n+1):
            result.append(len([(curr>>i)&1 for i in range(256) if (curr>>i)&1]))
        return result