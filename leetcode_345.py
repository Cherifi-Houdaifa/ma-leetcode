def main(s:str):
    vowels = "aeiouAEIOU"
    result = list(s)
    resultLen = len(result)
    left = 0
    right = resultLen - 1

    while left < right and left < resultLen and right >= 0:
        if result[left] in vowels and result[right] in vowels:
            # both left and right are in a vowel char so do the thing
            # switch the vowels
            temp = result[left]
            result[left] = result[right]
            result[right] = temp
            
            right -= 1
            left += 1
        elif result[left] in vowels:
            right -= 1
        elif result[right] in vowels:
            left += 1
        else:
            right -= 1
            left += 1
    return "".join(result)

main("leetcode")