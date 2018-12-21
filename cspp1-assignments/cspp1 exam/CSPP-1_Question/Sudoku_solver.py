"""
{ Sudoku_solver}
"""
Sudoku_solver = input()
grid = [True]*9
if '.' not in Sudoku_solver:
    print("Given sudoku is solved")
elif len(Sudoku_solver) != 81:
    print("Invalid input")
else:
    count = 0
    i = ""
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