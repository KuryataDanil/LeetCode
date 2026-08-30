
def simplifyPath(path: str) -> str:
    arr = path.split('/')
    res = []
    for i in arr:
        if i == ".." and len(res) != 0:
            res.pop(-1)
        elif i != '.' and i != '' and i != '..':
            res.append(i)
    return '/' + '/'.join(res)


print(simplifyPath("/home/"))
