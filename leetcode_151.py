def main(s: str):
    sLen = len(s)

    # remove trailing and leading spaces
    left = 0
    right = sLen - 1
    while left < right:
        if s[left] != " " and s[right] != " ":
            break
        elif s[left] != " ":
            right -= 1
        elif s[right] != " ":
            left += 1
        else:
            left += 1
            right -= 1

    s = s[left: right + 1]
    sLen = len(s)

    # loop through the newS
    i = 0
    result = ""
    currentWord = ""
    while i < sLen:
        if s[i] != " ":
            currentWord += s[i]
            if i == sLen - 1:
                if result == "":
                    result = currentWord
                else:
                    result = f"{currentWord} {result}"
                currentWord = ""
        elif s[i] == " " and currentWord != "":
            if result == "":
                result = currentWord
            else:
                result = f"{currentWord} {result}"
            currentWord = ""

        i += 1

    return result


main("a good   example")
