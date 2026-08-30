
def myAtoi(s: str) -> int:
    i = 0
    sign = 1
    lens = len(s)
    while i < lens and s[i] == " ":
        i += 1
    if i == lens:
        return 0

    if s[i] == "-" or s[i] == "+":
        if s[i] == "-":
            sign = -1
        i += 1
       
    res = "0"
    while i != len(s) and s[i].isdigit():
        res += s[i]
        i += 1

    res = int(res) * sign
    if res < -2**31:
        res = -2**31
    elif res > 2**31 - 1:
        res = 2**31 - 1

    return res
print(myAtoi("+1"))