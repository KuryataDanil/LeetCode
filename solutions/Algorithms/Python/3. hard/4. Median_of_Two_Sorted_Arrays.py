def findMedianSortedArrays(nums1, nums2) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    res = 0
    newarr = []
    n = 0
    m = 0
    while n < len1 and m < len2:
        if nums1[n] < nums2[m]:
            newarr.append(nums1[n])
            n += 1
        else:
            newarr.append(nums2[m])
            m += 1

    while n < len1:
        newarr.append(nums1[n])
        n += 1

    while m < len2:
        newarr.append(nums2[m])
        m += 1

    if (len1 + len2) % 2 == 1:
        res = newarr[(len1 + len2) // 2]
    else:
        res = (newarr[(len1 + len2) // 2] + newarr[(len1 + len2) // 2 - 1]) / 2
    return res

