class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = [x for x in range(len(nums))]
        backpack = zip(nums, indexes) # keep track of original positions

        # Sorting allows us to use binary search
        # By sorting the original list with the indexes,
        # we have a way of figuring out where each value was in the original array.
        b = sorted(backpack, key=lambda x: x[0])

        for i, n in enumerate(b):
            j = bisect_left(b, target - n[0], lo=i+1, key=lambda x: x[0])
            # bin search gives potential index, we need to check if sum is correct
            if j < len(nums) and b[j][0] + n[0] == target:
               return [b[i][1], b[j][1]] # get indexes of original array
        