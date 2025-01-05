class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def aux(s_i, t_i):
            if t_i == len(t):
                return s_i == len(s)
            if s_i == len(s):
                return True
            
            if s[s_i] == t[t_i]:
                return aux(s_i + 1, t_i + 1)
            else:
                return aux(s_i, t_i + 1)
    
        return aux(0, 0)

