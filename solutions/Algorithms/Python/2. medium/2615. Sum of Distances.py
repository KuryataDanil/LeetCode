class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        num_indices = dict()
        d = dict()
        for i, num in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = i
                d[num] = 1
            else:
                num_indices[num] = num_indices[num] + i
                d[num] = d[num] + 1
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = num_indices[nums[i]] - d[nums[i]] * i
            num_indices[nums[i]] = num_indices[nums[i]] - 2 * i
            d[nums[i]] = d[nums[i]] - 2

        return res
