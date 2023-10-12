def main(s: str, numRows: int):
    # input: "PAYPALISHIRING", 3
    #         12321232123212
    #          
    #            
    """
        P   A   H   N
        A P L S I I G
        Y   I   R
    """
    # input: "PAYPALISHIRING", 4
    #         12   2 2 1 2    1
    """
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
    """
    # test: PAYP, 3

    zigzag = ["" for i in range(numRows)]
    i = 0
    rowIndex = 0
    sLen = len(s)

    increment = 1

    while i < sLen:
        zigzag[rowIndex] += s[i]
        if rowIndex >= numRows - 1:
            increment = -1
        elif rowIndex <= 0:
            increment = 1

        rowIndex += increment
        i += 1
    
    result = ""
    for i in zigzag:
        result += i

    return result
main("PAYPALISHIRING", 4)
