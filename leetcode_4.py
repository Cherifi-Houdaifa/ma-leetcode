def main(nums1: list[int], nums2: list[int]) -> float | None:
    # input: [1, 3], [2]
    # output: 2
    nums1Len = len(nums1)
    nums2Len = len(nums2)
    result = []
    i = 0
    j = 0
    while True:
        if i >= nums1Len and j >= nums2Len:
            break
        elif i >= nums1Len:
            result.append(nums2[j])
            j += 1
            continue
        elif j >= nums2Len:
            result.append(nums1[i])
            i += 1
            continue
        num1 = nums1[i]
        num2 = nums2[j]
        if num1 < num2:
            result.append(num1)
            i += 1
        elif num1 == num2:
            result.append(num1)
            result.append(num1)
            i += 1
            j += 1
        else:
            result.append(num2)
            j += 1

    resultLen = nums1Len + nums2Len
    middle = int(resultLen / 2)
    if resultLen % 2 == 0:
        # length is even
        return (result[middle] + result[middle - 1]) / 2
    else:
        # length is odd
        return result[middle]


print(main([1, 2], [3, 4]))
