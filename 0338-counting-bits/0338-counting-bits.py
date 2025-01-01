class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            result = [0, 1]
            for i in range(2, n+1):
                result.append(result[i - (2 ** floor(log2(i)))] + 1)
            return result