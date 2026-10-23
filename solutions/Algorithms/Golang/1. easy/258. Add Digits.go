/*
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
*/

func addDigits(num int) int {
    for num / 10 > 0 {
        cur := num
        res := 0
        for cur > 0 {
            res += cur % 10
            cur /= 10
        }
        num = res
    }

    return num
}