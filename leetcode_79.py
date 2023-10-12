def main(board: list[list[str]], word: str):
    # input: [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "CCF"
    # output: true
    rows = len(board)
    cols = len(board[0])

    i = 0
    j = 0
    while i < rows:
        j = 0
        while j < cols:
            result = findWord(board, word, i, j, rows, cols, [])
            if result:
                return True
            j += 1
        i += 1
    return False

def findWord(board: list[list[str]], word: str, k: int, l: int, rows: int, cols: int, usedCells: list[tuple[int, int]]):
    # this is a recuresive function
    wordLen = len(word)
    if wordLen == 0:
        return True

    if board[k][l] == word[0]:
        copy = usedCells.copy()
        copy.append((k, l))
        adjacent = getAdjacent(k, l, rows, cols, copy)
        if not adjacent and wordLen == 1:
            return True
        for k, l in adjacent:
            result = findWord(board, word[1:], k, l, rows, cols, copy)
            if result:
                return True
    else:
        return False


def getAdjacent(i: int, j: int, rows: int, cols: int, usedCells: list[tuple[int, int]]):
    adjacent = []
    if 0 <= i+1 < rows and (i + 1, j) not in usedCells:
        adjacent.append((i + 1, j))
    if 0 <= i-1 < rows and (i - 1, j) not in usedCells:
        adjacent.append((i - 1, j))
    if 0 <= j+1 < cols and (i, j + 1) not in usedCells:
        adjacent.append((i, j+1))
    if 0 <= j-1 < cols and (i, j - 1) not in usedCells:
        adjacent.append((i, j - 1))
    return adjacent