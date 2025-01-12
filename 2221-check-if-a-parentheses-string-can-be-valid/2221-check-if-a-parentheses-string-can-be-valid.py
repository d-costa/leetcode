class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        if s == "()":
            return True

        if (s[0] == ")" and locked[0] == "1") or (s[-1] == "(" and locked[-1] == "1"):
            return False

        unlocked = []
        opened = []

        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                opened.append(i)
            else:
                if len(opened) > 0:
                    opened.pop()
                elif len(unlocked) > 0:
                    unlocked.pop()
                else:
                    return False

        while opened and unlocked:
            if opened[-1] < unlocked[-1]:
                opened.pop()
                unlocked.pop()
            else:
                break
        if len(opened) > 0:
            return False # unmatched
        return True
