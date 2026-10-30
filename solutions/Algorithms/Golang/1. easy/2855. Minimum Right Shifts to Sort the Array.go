/*
You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum number of right shifts required to sort nums and -1 if this is not possible.

A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.
*/

func minimumRightShifts(nums []int) int {
    n := len(nums)
    if n < 2 {
        return 0
    }

    breaks := 0
    breakIndex := -1

    for i := 0; i < n-1; i++ {
        if nums[i] > nums[i+1] {
            breaks++
            breakIndex = i
        }
    }

    if breaks == 0 {
        return 0
    }

    if breaks > 1 {
        return -1
    }

    if nums[n-1] > nums[0] {
        return -1
    }

    return n - breakIndex - 1
}
