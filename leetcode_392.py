def main(s: str, t: str):
    sLen = len(s)
    tLen = len(t)

    sIndex = 0
    tIndex = 0

    while 1:
        if sIndex >= sLen:
            return True
        if tIndex >= tLen and sIndex < sLen:
            return False
        if s[sIndex] == t[tIndex]:
            sIndex+= 1
            tIndex+=1
        elif s[sIndex] != t[tIndex]:
            tIndex+= 1
        

print(main("abc", "ahbgd"))