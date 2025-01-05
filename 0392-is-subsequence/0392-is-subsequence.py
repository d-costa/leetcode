class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return aux(s, t)

def aux(s, t):
    if len(t) == 0:
      return len(s) == 0
    if len(s) == 0:
        return True
    
    if s[0] == t[0]:
        return aux(s[1:], t[1:])
    else:
        return aux(s, t[1:])