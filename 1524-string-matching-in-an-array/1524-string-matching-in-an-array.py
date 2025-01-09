class Solution:
    # KMP, worse in this case than brute force or std lib's str.count
    def stringMatching(self, words: List[str]) -> List[str]:
        found = []
        for word in words:
            pattern = substring_search(word)
            for w in words:
                if (
                    word != w
                    and len(word) < len(w)
                    and (not word in found)
                    and compare_match(word, w, pattern)
                ):
                    found.append(word)
        return found


# true if word is substring of w
def compare_match(word, w, pattern):
    i = 0  # iterates word, the potential substring
    j = 0  # iterates w

    while True:
        if j == len(w):
            return False  # exhausted w

        if word[i] != w[j]:
            i = pattern[max(0, i - 1)]  # go back in w

        if word[i] == w[j]:
            if i == len(word) - 1:
                return True  # matched entire word
            i = i + 1
            j = j + 1
        else:
            j = j + 1  # try to find substring further along in w


def substring_search(s: string) -> List[int]:
    aux = [None] * len(s)
    aux[0] = 0

    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j]:
            if j == 0:
                break
            j = aux[j - 1]

        if s[i] == s[j]:
            aux[i] = j + 1
            i = i + 1
            j = j + 1
        else:
            aux[i] = 0
            i = i + 1

    return aux
