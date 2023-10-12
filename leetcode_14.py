def main(strs: list[str]):
    strsLen = len(strs)
    charIndex = 0
    maxCharIndex = len(min(strs))
    stop = False
    while charIndex < maxCharIndex:
        strIndex = 0
        while strIndex < strsLen - 1:
            print(strIndex)
            if strs[strIndex][charIndex] != strs[strIndex+1][charIndex]:
                stop = True
                break
            strIndex+= 1
        if stop:
            break
        charIndex += 1
    return strs[0][:charIndex]

print(main(["", ""]))