"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
    raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
    raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
    raise an exception
"""
def inputvalidation(sudoku1):
    if len(sudoku1) != 81:
        raise Exception("Invalid input")
    elif '.' not in sudoku1:
        raise Exception("Given sudoku is solved")

def validateSudoku(sudoku):
    for i in range(8):
        var = getRowValues(i, sudoku)
        var1 = getColumnValues(i, sudoku) 
        duplicates = set(var)
        dup2 = set(var1)
        if len(var) != len(duplicates):
            raise Exception("Invalid Sudoku:Duplicate values")
        if len(var1) != len(dup2):
            raise Exception("Invalid Sudoku:Duplicate values")
            #print(var)

"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(cell, sudoku):
    row = []
    for i in sudoku[cell]:
        if i != '.':
            row.append(i)
    #print(row)
    return row

"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(cell, sudoku):
     col = []
     for row in sudoku:
        if row[cell] != '.':
         col.append(row[cell])
     return col
    #pass


"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues(row, col, sudoku):
    subgrid = []
    var = False
    for i in range(0, 3):
        for j in range(0, 3):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(0, 3):
        for j in range(3, 6):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(0, 3):
        for j in range(6, 9):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(3, 6):
        for j in range(0, 3):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(3, 6):
        for j in range(3, 6):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(3, 6):
        for j in range(6, 9):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(6, 9):
        for j in range(0, 3):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(6, 9):
        for j in range(3, 6):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid

    subgrid = []
    for i in range(6, 9):
        for j in range(6, 9):
            if i == row and j == col:
                var = True
            subgrid.append(sudoku[i][j])
    if var == True:
        return subgrid
    #pass
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == '.':
                row = getRowValues(i, sudoku)
                col = getColumnValues(j, sudoku)
                grid = getGridValues(i, j, sudoku)
                totalgrid = row + col + grid
                str1 = ''
                for k in range(1,10):
                    if str(k) not in totalgrid:
                        str1 += str(k)
                print(str1) 



    #pass
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
    sudoku = list(input())
    #print(sudoku)
    #grid = list(sudoku)
    #print(type(grid))
    list1 = []
    try:
        for i in range(0,81,9):
            lst2 = []
            for j in range(0,9):
                lst2.append(sudoku[i])
                i = i +1

            list1.append(lst2)
            inputvalidation(sudoku)
        validateSudoku(list1)
        possibleValues(list1)

    except Exception as e:
        print(e)
    #print(list1)



if __name__ == '__main__':
    main()
    ##
    ## { item_description }
    ##
    
