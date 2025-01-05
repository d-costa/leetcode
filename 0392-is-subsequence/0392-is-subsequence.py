class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True
        if s == "": return True
        
        s_len = len(s)
        t_len = len(t)

        def aux(s_i, t_i):
            if t_i == t_len:
                return s_i == s_len
            if s_i == s_len:
                return True
            
            if s[s_i] == t[t_i]:
                return aux(s_i + 1, t_i + 1)
            else:
                return aux(s_i, t_i + 1)
    
        return aux(0, 0)

