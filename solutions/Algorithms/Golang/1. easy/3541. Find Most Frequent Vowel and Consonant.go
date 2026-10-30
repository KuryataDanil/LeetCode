/*
You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
*/



func maxFreqSum(s string) int {
    vowel := map[rune]int{}
    consonant := map[rune]int{}
    isVowel := func(r rune) bool {
        return r == 'a' || r == 'e' || r == 'i' || r == 'o' || r == 'u'
    }
    for _, r := range s {
        if isVowel(r){
            vowel[r]++
        } else {
            consonant[r]++
        }
    }

    maxV, maxC := 0, 0
    for _, c := range vowel {
        if c > maxV { maxV = c }
    }

    for _, c := range consonant {
        if c > maxC { maxC = c }
    }

    return maxV + maxC
}
