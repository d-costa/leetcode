class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = [x for x in range(len(nums))]
        backpack = zip(nums, indexes) # keep track of original positions

        # Sorting allows us to use binary search
        # By sorting the original list with the indexes,
        # we have a way of figuring out where each value was in the original array.
        b = sorted(backpack, key=lambda x: x[0])

        # Example:
        # nums = [3,2,4]
        # indexes = [0, 1, 2]
        # backpack = [(3, 0), (2, 1), (4, 2)]
        # b = [(2, 1), (3, 0), (4, 2)]

        # We find that 2 + 4 = target (6)
        # 2 had index 1, and 4 had index 2.
        # return [1, 2]

        for i, n in enumerate(b):
            j = bisect_left(b, target - n[0], lo=i+1, key=lambda x: x[0])
            # bin search gives potential index, we need to check if sum is correct
            if j < len(nums) and b[j][0] + n[0] == target:
               return [b[i][1], b[j][1]] # get indexes of original array
        