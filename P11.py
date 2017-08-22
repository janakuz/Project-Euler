f = open('P11.txt', 'r')
grid = f.readlines()
f.close()
grid = [row.split(' ') for row in grid]
for row in range(len(grid)):
    grid[row] = [int(i) for i in grid[row]]

maxProduct = 0

def traverseDiagonally(startRow, startColumn, d):
    global maxProduct
    product = grid[startRow][startColumn]*grid[startRow+1][startColumn+1*d]*grid[startRow+2][startColumn+2*d]*grid[startRow+3][startColumn+3*d]
    if (startRow == 0):
        j = startColumn
        for i in range(1, len(grid)-startRow-startColumn-4):
            if (product > maxProduct):
                maxProduct = product
            if(grid[i-1][j] != 0):
                product = product/grid[i-1][j]*grid[i+3][j+4*d]
            else:
                product = grid[i][j+1*d]*grid[i+1][j+2*d]*grid[i+2][j+3*d]*grid[i+3][j+4*d]
            j += d

    elif (startColumn == 0):
        i = startRow
        for j in range(1, len(grid)-startRow-startColumn-4):
            if (product > maxProduct):
                maxProduct = product
            if(grid[i][j-1] != 0):
                product = product/grid[i][j-1]*grid[i+4][j+3]
            else:
                product = grid[i+1][j]*grid[i+2][j+1]*grid[i+3][j+2]*grid[i+4][j+3]
            i += 1

    elif (startColumn == 19):
        i = startRow
        for j in range(len(grid)-startRow, 3):
            if (product > maxProduct):
                maxProduct = product
            if(grid[i][j+1] != 0):
                product = product/grid[i][j+1]*grid[i+4][j-3]
            else:
                product = grid[i+1][j]*grid[i+2][j-1]*grid[i+3][j-2]*grid[i+4][j-3]
            i += 1            
    if (product > maxProduct):
        maxProduct = product
        

for i in range(len(grid)):
    product = grid[i][0]*grid[i][1]*grid[i][2]*grid[i][3]
    for j in range(1, len(grid)-3):
        if (product > maxProduct):
            maxProduct = product
        if (grid[i][j-1] != 0):
            product = product/grid[i][j-1]*grid[i][j+3]
        else:
            product = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]

        #main diagonals (LtR)
        if (j <= 16 and i <= 16):
            traverseDiagonally(i,j,1)
        #minor diagonals (RtL)
        if (j >= 3 and i <= 16):
            traverseDiagonally(i,j,-1)
    if (product > maxProduct):
        maxProduct = product

for j in range(len(grid)):
    product = grid[0][j]*grid[1][j]*grid[2][j]*grid[3][j]
    for i in range(1, len(grid)-3):
        if (product > maxProduct):
            maxProduct = product
        if (grid[i-1][j] != 0):
            product = product/grid[i-1][j]*grid[i+3][j]
        else:
            product = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]

        #main diagonals (LtR)
        if (i <= 16 and j <= 16):
            traverseDiagonally(i,j,1)
        #minor diagonals (RtL)
        if (i <= 16 and j >= 3):
            traverseDiagonally(i,j,-1)
    if (product > maxProduct):
        maxProduct = product



