def main(s: str, k: int):
    left = 0
    right = k - 1
    def getVowelCount(string: str) -> int:
        count = 0
        for i in string:
            if i in "aeiou":
                count+=1
        return count
    
    sLen = len(s)
    currentCount = 0
    maxCount = -1
    while right < sLen:
        if left == 0:
            maxCount = getVowelCount(s[left: right + 1])
            currentCount = maxCount
        else:

            if s[left - 1] in "aeiou":
                currentCount -= 1
            if s[right] in "aeiou":
                currentCount += 1
            if currentCount > maxCount:
                maxCount = currentCount

        right += 1
        left += 1
    return maxCount

print(main("abciiidef", 3))