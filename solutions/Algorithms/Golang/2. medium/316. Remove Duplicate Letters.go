package main

/*
Given a string s, remove duplicate letters so that every letter appears once and only once.
The relative order of the letters that were not removed must be preserved.
You must make sure your result is the smallest in lexicographical order among all possible results.

*/

func removeDuplicateLetters(s string) string {
	lastOccurrence := make(map[rune]int)
	for i, r := range s {
		lastOccurrence[r] = i
	}

	inStack := make(map[rune]bool)
	stack := []rune{}

	for i, r := range s {
		if inStack[r] {
			continue
		}

		for len(stack) > 0 &&
			stack[len(stack)-1] > r &&
			lastOccurrence[stack[len(stack)-1]] > i {
			removed := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			inStack[removed] = false
		}

		stack = append(stack, r)
		inStack[r] = true
	}

	return string(stack)
}
