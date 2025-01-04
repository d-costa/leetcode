class Solution:

    def countPalindromicSubsequence(self, substr: str) -> int:
        total = 0
        for c in ascii_lowercase:
            start = float("inf")
            end = float("-inf")
            
            for i, s in enumerate(substr):

                if s == c:
                    if i < start:
                        start = i
                    if i > end:
                        end = i

            if isinstance(start, int) and isinstance(end, int) and start < end:
                total = total + len(set(substr[start+1:end]))
                    
        return total





 
