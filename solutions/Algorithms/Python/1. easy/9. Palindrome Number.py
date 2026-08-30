def isPalindrome(x: int) -> bool:
    return str(x)[:len(str(x)) // 2] == (str(x)[len(str(x)) // 2:])[::-1] if len(str(x)) % 2 == 0 else str(x)[:len(str(x)) // 2] == (str(x)[len(str(x)) // 2 + 1:])[::-1] 
print(isPalindrome(-1221))
