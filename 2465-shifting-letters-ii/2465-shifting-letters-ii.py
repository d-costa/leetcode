class Solution:

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff_arr = [0] * (len(s) + 1)

        for shift in shifts:
            #approach 1
            diff_arr[shift[0]] = diff_arr[shift[0]] + (1 if shift[2] == 1 else -1)
            diff_arr[shift[1] + 1] = diff_arr[shift[1] + 1] + (- 1 if shift[2] == 1 else 1)

        prefix_sum = 0
        result = ""

        for i, c in enumerate(s):
            prefix_sum = prefix_sum + diff_arr[i]
            # A = 97
            # Z = 122
            result = result + chr((ord(c) - 97 + prefix_sum) % (122 - 97 + 1) + 97)

        return result