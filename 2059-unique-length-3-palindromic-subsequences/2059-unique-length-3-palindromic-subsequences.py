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
                found = set()
                for i in range(start + 1, end):
                    
                    found.add(substr[i])
                    if len(found) == 26:
                        break
    
                total = total + len(found)
                    
        return total





 
