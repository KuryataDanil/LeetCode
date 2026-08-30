def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        #if i < len(nums) - 1 and nums[i] == nums[i + 1]:
         #   continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            # print(i, l, r)
            num = nums[i] + nums[l] + nums[r]
            if num == 0 and [nums[i], nums[l], nums[r]] not in res:
                res.append([nums[i], nums[l], nums[r]])
                r -= 1
                l += 1
            elif num > 0:
                r -= 1
            else:
                l += 1
           
    return res


print(threeSum([0,0,0,0]))
