def intToRoman(num: int) -> str:
    res = ""
    while num // 1000 != 0:
        res += "M"
        num -= 1000
    
    if num // 100 == 9:
        res += "CM"
        num -= 900
    elif num // 100 == 4:
        res += "CD"
        num -= 400
    if num // 100 > 5:
        res += "D"
        num -= 500
    while num // 100 != 0:
        res += "C"
        num -= 100

    if num // 10 == 9:
        res += "XC"
        num -= 90
    elif num // 10 == 4:
        res += "XL"
        num -= 40
    if num // 10 > 5:
        res += "L"
        num -= 50
    while num // 10 != 0:
        res += "X"
        num -= 10

    if num == 9:
        res += "IX"
        num -= 9
    elif num == 4:
        res += "IV"
        num -= 4
    if num > 5:
        res += "V"
        num -= 5
    while num != 0:
        res += "I"
        num -= 1
    return res

print(intToRoman(3922))