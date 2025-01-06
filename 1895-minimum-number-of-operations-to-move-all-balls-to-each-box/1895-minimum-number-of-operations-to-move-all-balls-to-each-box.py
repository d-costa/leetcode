class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        for i, bucket in enumerate(boxes):
            if bucket == '1':   
                for j in range(n):
                    result[j] = result[j] + abs(j-i)
        return result
        