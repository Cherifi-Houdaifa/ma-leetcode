def main(s: str) -> int:
    result = 0

    i = 0
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    while i < len(s):
        char = s[i]
        if char == "I":
            result += 1
        elif char == "V":
            result += 5
        elif char == "X":
            result += 10
        elif char == "L":
            result += 50
        elif char == "C":
            result += 100
        elif char == "D":
            result += 500
        elif char == "M":
            result += 1000

        i += 1
    return result


main("MCMXCIV")
