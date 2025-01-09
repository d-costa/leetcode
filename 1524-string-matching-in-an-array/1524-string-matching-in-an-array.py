class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            if any((word != w and word in w) for w in words):
                result.append(word)
        return result
        