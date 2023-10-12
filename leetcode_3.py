def main(s: str):
    longest = ""
    tempLongest = ""
    stringIndex = 0

    while len(s) > 2 * len(longest):
        if (stringIndex >= len(s)):
            longest = tempLongest
            break

        if stringInculdes(tempLongest, s[stringIndex]):
            if len(tempLongest) > len(longest):
                longest = tempLongest
            tempLongest = ""
            stringIndex = 0
            s = s[1:]
        else:
            tempLongest += s[stringIndex]
            stringIndex += 1
    return len(longest)


def stringInculdes(string: str, char: str):
    for i in string:
        if char == i:
            return True
    return False
