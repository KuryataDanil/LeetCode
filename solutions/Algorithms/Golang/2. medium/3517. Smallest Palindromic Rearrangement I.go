import (
	"fmt"
	"strings"
)

func smallestPalindrome(s string) string {
	if len(s) == 1 {
		return s
	}

	mass := [26]int{}

	for _, r := range s {
		mass[r-97]++
	}

	//fmt.Println(mass)

	var res strings.Builder

	centerLetter := ""

	for i := range mass {
		if mass[i]%2 != 0 {
			centerLetter = string(i + 97)
		}

		res.WriteString(strings.Repeat(string(i+97), mass[i]/2))
	}

	buf := res.String()
	res.WriteString(centerLetter)
	res.WriteString(reverseString(buf))

	return res.String()

}

func reverseString(s string) string {
	runes := []rune(s)

	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}
