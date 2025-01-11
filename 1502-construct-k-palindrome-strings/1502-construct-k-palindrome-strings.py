class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False # no chars to produce k groups

        freq = Counter(s)

        odd_freqs = [c for c in freq if freq[c] % 2 == 1]
        if len(odd_freqs) > k:
            return False # we need at least k groups to put odd chars in

        return True
