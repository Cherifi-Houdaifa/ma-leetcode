def main(rowSum: list[int], colSum: list[int]):

    rows = len(rowSum)
    cols = len(colSum)

    matrix: list[list[int]] = createMatrix(rows, cols)

    currentRowSum = [0 for i in range(rows)]
    currentColSum = [0 for i in range(cols)]
    rowIndex = 0
    colIndex = 0
    while rowIndex < rows:
        while colIndex < cols:
            # set the value of the current cell to the maximum value that can be set
            currentCellValue = min([rowSum[rowIndex], colSum[colIndex]])

            # ---| check row |---
            if currentRowSum[rowIndex] + currentCellValue > rowSum[rowIndex]:
                currentCellValue = rowSum[rowIndex] - currentRowSum[rowIndex]

            # ---| check col |---
            if currentColSum[colIndex] + currentCellValue > colSum[colIndex]:
                currentCellValue = colSum[colIndex] - currentColSum[colIndex]

            matrix[rowIndex][colIndex] = currentCellValue
            currentRowSum[rowIndex] += currentCellValue
            currentColSum[colIndex] += currentCellValue

            colIndex += 1
        colIndex = 0
        rowIndex += 1

    return matrix
    



def createMatrix(rows: int, cols: int):
    # create matrix of rows and columns
    # all elements are 0
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)

    return matrix

print(main([4,12,10,1,0], [1,0,3,16,7]))
# output: [[1, 0, 3, 0, 0], [0, 0, 0, 12, 0], [0, 0, 0, 4, 6], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]

"""
[
     a, b, c
   e[1, 2, 3],
   f[4, 5, 6],
   g[7, 8, 9],  
]
a + b + c = e +f + g
"""



"""
Given two one dimensional arrays
Make a function
That returns a matrix that has a numbers of rows equal to the length of the first array
And a number of columns equal to the length of the second array
Such that
If you sum the integers of the first row you will get the first value of the rowSum array
And if you sum the integers of the first column you get the first value of the colSum array
So the rowSum arrays represents the sum of the rows
And the colSum array represents the sum of the columns
The rules
All the values in the input and output are positive integers
Got it
"""