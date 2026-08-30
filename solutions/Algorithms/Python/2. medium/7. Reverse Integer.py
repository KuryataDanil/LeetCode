def reverse(x: int) -> int:
    if x < 0:
        res = int((str(x)[1:])[::-1]) * -1  
    else:
        res = int(str(x)[::-1])
    return res if res <= 2**31 - 1 and res >= -2**31 else 0
print(reverse(-123))


