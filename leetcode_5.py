def main(s: str):
    # input: "hgog"
    # output: "gog"
    
    # not a brute force implementation
    pass

def checkPal(s: str):
    i = 0
    sLen = len(s)
    while i < sLen:
        if s[i] != s[sLen - 1 - i]:
            return False
        i += 1
    return True
