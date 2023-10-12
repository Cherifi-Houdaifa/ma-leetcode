def main(chars: list[str]):
    s = []
    charsLen = len(chars)
    addAtEnd = False
    currentSequence = []
    i = 0
    while i < charsLen:
        currentChar = chars[i]
        if currentSequence:
            if currentChar == currentSequence[0] and i < charsLen - 1:
                currentSequence.append(currentChar)
            else:
                currentSequenceLen = len(currentSequence)
                if i == charsLen - 1:
                    if currentChar == currentSequence[0]:
                        currentSequenceLen += 1
                    else:
                        addAtEnd = True
                if currentSequenceLen == 1:
                    s.extend([currentSequence[0]])
                else:
                    s.append(currentSequence[0])
                    s.extend(list(str(currentSequenceLen)))
                currentSequence = [currentChar]
                if addAtEnd:
                    s.append(currentChar)
        else:
            if 0 == charsLen - 1:
                s.append(currentChar)
            currentSequence = [currentChar]
        i += 1
    i = 0
    while i < len(s):
        chars[i] = s[i]
        i += 1
    return len(s)


main(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
