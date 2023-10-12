def main(x: int):
    if x == 0:
        return 0

    negative = False
    if x < 0:
        x = -x
        negative = True

    while 1:
        if getFirstDigit(x) == 0:
            x = int(x / 10)
        else:
            break

    result = 0
    xLen = len(str(x))
    i = 0
    while i < xLen:
        digit = getFirstDigit(x)
        result += digit * pow(10, xLen - (i + 1))
        x = int(x / 10)
        i += 1
    
    if result < -(2**31) or result > 2**31 - 1:
        return 0
    
    if negative:
        return -result
    return result


def getFirstDigit(num: int):
    result = num
    count = 1
    while (len(str(result)) > 1):
        result -= int(result / pow(10, len(str(result)) - count)
                      ) * pow(10, len(str(result)) - count)

    return result


print(main(-123))
# check if number is negative and remove the minus
# remove the zeros at the right
