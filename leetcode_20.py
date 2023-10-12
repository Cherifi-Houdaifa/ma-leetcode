def main(s: str):
    opposites = {
        ")": "(",
        "}":"{",
        "]":"["
    }
    stack = []

    sLen = len(s)
    i = 0
    while i < sLen:
        if s[i] in "({[":
            stack.append(s[i])
        else:
            stackLen = len(stack)
            if stackLen == 0:
                return False
            if stack[stackLen - 1] == opposites[s[i]]:
                stack = stack[0:stackLen - 1]
            else:
                return False
        i+=1
    if len(stack) == 0:
        return True
    return False
print(main("]"))
# print(main("()"))
# print(main("([])"))
