
def validPartition(nums: list[int]) -> bool:
    return Part(nums, 1)
        

def Part(nums: list[int], index: int) -> bool:
    for i in range(index, len(nums)):
        if abs(nums[i - 1] - nums[i]) <= 1:
            continue
        if i - index <= 1:
            return False
        print(i)
        return Part(nums, i)
    print(index)
    return True if len(nums) - index > 1 and index != 1 else False

print(validPartition([1,1,1,2]))