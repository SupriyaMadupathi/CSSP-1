def check():
    inpu = input()
    grid= []
    
    for i in inpu:
        grid.append(i)
    
    matrix = [9][9]
    print(grid)
    i = 0
    flag = False
    for j in range(9):
        ls = []
        for k in range(9):
            
            ls.append(grid[i]);
            i = i+1
        matrix.append(ls)
    for i in range(9):
        if "." not in matrix[i][j]:
            flag = True
    if flag:
        print("Given sudoku is solved")