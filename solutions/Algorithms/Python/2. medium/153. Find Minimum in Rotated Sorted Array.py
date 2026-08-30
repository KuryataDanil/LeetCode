class Solution:
    def findMin(self, nums: list[int]) -> int:
        r = len(nums) - 1
        l = 0
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            # print(l, mid, r)
        return nums[l]


print(Solution().findMin([3, 4, 5, 1, 2]))
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin([2, 3, 1]))