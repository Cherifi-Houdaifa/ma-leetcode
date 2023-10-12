def main(x: int) -> bool:
    if x < 0:
        return False
    y = x
    reversedX = 0

    while x > 0:
        digit = getFirstDigit(x)
        reversedX += digit * pow(10, len(str(x)) - 1)

        x = int(x / 10)
    if y == reversedX:
        return True
    return False


def getFirstDigit(num: int):
    result = num
    count = 1
    while (len(str(result)) > 1):
        result -= int(result / pow(10, len(str(result)) - count)
                      ) * pow(10, len(str(result)) - count)
    return result

print(main(1221))
