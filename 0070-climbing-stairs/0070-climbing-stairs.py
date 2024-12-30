import math

class Solution:
    def climbStairs(self, n: int) -> int:
        combinations = 0
        for i in range(0, n//2 + 1):
            combinations = combinations + math.comb(n-i, i)
        return combinations
