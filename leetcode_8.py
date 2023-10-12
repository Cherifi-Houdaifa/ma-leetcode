def main(s: str):
    # ignore any leading white space
    # check if the first char is + or - (default is positive if none is present)
    # read the chars until you reach a none digit char and ignore the rest
    # convert the resulted string to a int
    # make sure the int is a 32 bit signed int
    s = s.lstrip()
    positive = True
    positiveSet = False
    firstNumIndex: int | None = None
    resultString = ""
    for i in s:
        if i in "0123456789":
            if firstNumIndex == None:
                firstNumIndex = s.index(i)
            resultString += i
        else:
            if firstNumIndex == None:
                # still has not reached first number
                if i == "+" and not positiveSet:
                    positiveSet = True
                elif i == "-" and not positiveSet:
                    positive = False
                    positiveSet = True
                else:
                    break
            else:
                break
    if len(resultString) == 0:
        return 0

    result = 0
    i = 0

    resultStringLen = len(resultString)
    while i < resultStringLen:
        result += int(resultString[i]) * pow(10, resultStringLen - 1 - i)
        
        i += 1
    if not positive:
        result = -result
    if result < -(2**31):
        return -(2**31)
    elif result > 2**31 - 1:
        return 2**31 - 1
    return result

print(main("21474836460"))