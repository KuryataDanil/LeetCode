def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1 
    res = 0
    while left < right:
        cur = (right - left) * min(height[left], height[right])
        if cur > res:
            res = cur
        if height[left] < height[right]:
            left += 1
        else:
            right += 1
    return res