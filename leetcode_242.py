def main(s: str, t: str):
    if len(s) != len(t):
        return False
    chars = dict()
    for char in s:
        chars[char] = 0
    for char in s:
        chars[char] +=1
    for char in t:
        try:
            if chars[char] > 0:
                chars[char] -= 1
            else:
                return False
        except KeyError:
            return False
        
    return True
        

print(main("anagram", "nagaram"))