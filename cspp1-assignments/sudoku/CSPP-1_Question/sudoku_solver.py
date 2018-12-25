sudoku = input()
if len(sudoku) != 81:
    print("Invalid input")
elif '.' not in sudoku:
    print("Given sudoku is solved")
else:
    i = ""
    grid = list(sudoku)
    list1 = []
    list2 = []
    count = 0
    for i in Sudoku_solver:
        if count == 9:
            for j in range(9):
                if grid[j] == True:
                    print(j+1)
            grid = [True]*9
            count = 0
        count = count + 1
        if i == '.':
            continue
        grid[int(i) - 1] = False
    if count == 9:
            for j in range(9):
                if grid[j] == True:
                    print(j+1)
            grid = [True]*9
            count = 0
    #print(grid)
    #for i in range(len(grid)):
        #print(grid)
    #   list1.append(grid[i])
    #   print(list1)
        #for i in list1:
        #   count[i] += 1
        #   if count[1] == 2:
        #       print("Invalid Sudoku:Duplicate values")
