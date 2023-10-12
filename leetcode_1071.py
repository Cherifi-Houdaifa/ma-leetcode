def main(str1: str, str2: str):
    str1Len = len(str1)
    str2Len = len(str2)

    # greatest common divisor
    gcdLen = getGcd(str1Len, str2Len)
    gcd = ""
    i = 0
    while i < str1Len and i < str2Len:
        if str1[i] == str2[i]:
            gcd += str1[i]
            ratio1 = str1Len / len(gcd)
            ratio2 = str2Len / len(gcd)

            # this checks if both ratio 1 and 2 are integers
            if str(ratio1) == f"{int(ratio1)}.0" and str(ratio2) == f"{int(ratio2)}.0":
                if gcd * int(ratio1) == str1 and gcd * int(ratio2) == str2:
                    if len(gcd) < gcdLen:
                        i+= 1
                        continue
                    else:
                        return gcd
        else:
            break
        i += 1

    return ""
def getGcd(a, b):
 
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # Base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return getGcd(a-b, b)
    return getGcd(a, b-a)

# print(main("ABAB", "ABABABAB"))
print(main("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
# print(main("ABCDEF", "ABC"))
