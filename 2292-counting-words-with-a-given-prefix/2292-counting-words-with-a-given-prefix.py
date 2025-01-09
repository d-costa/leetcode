class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        found = 0
        for w in words:
            if w.startswith(pref):
                found = found + 1
        return found
        