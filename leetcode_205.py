def main(s: str, t: str):
    strLen = len(s)

    letterMap = dict()
    i = 0
    while i < strLen:
        sChar = s[i]
        tChar = t[i]
        if sChar in letterMap.keys():
            if letterMap[sChar] != tChar:
                return False
        else:
            if tChar in letterMap.values():
                return False
            letterMap[sChar] = tChar

        i += 1
    return True
print(main("badc", "baba"))