class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        w2_tally = Counter()

        for w in words2:
            w2_tally = w2_tally | Counter(w)

        
        def is_universal(w):
            w_freq = Counter(w)
            for c in w2_tally:
                if c not in w_freq or w2_tally[c] > w_freq[c]:
                    return False
            return True

        universal = set()
        for w1 in words1:
            if is_universal(w1):
                universal.add(w1)

        return list(universal)
