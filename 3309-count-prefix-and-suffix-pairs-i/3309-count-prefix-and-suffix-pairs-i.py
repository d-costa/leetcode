class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                count = count + self.isPrefixAndSuffix(words[i], words[j])
        return count

    def isPrefixAndSuffix(self, str1, str2) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)
        