def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s;
    arr = ["" for _ in range(numRows)]
    i = 0
    step = 1
    for char in s:
        arr[i] += char
        i += step
        if i == numRows - 1 or i == 0:
            step *= -1
    return ''.join(arr[i] for i in range(numRows))



print(convert("PAYPALISHIRING", 4))

##  "PAHNAPLSIIGYIR"



    



