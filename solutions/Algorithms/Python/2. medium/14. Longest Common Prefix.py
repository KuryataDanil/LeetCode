def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    lens = len(min(strs,key= lambda x: len(x)))
    i = 0
    while i < lens:
        for j in range(len(strs) - 1):
            if strs[j][i] != strs[j+1][i]:
                return res
        res += strs[0][i]
        i += 1
    return res


print(longestCommonPrefix(["flower","flow","flight"]))