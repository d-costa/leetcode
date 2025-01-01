class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 1 if s[0] == "0" else 0
        right_score = sum([int(c) for c in s[1:] if c])
        best_score = left_score + right_score
    
        for i in range(1, len(s)-1):
            if s[i] == "1":
                right_score = right_score - 1
            else:
                left_score = left_score + 1
            if best_score < left_score + right_score:
                best_score = left_score + right_score
        return best_score



        