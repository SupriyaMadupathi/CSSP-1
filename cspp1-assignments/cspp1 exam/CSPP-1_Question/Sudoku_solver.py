def check():
    values = input()
    li= []
    for i in values:
        li.append(i)
    matrix = []
    matrix = [9][9]
    print(li)
    i = 0
    flag = False
    for j in range(9):
        ls = []
        for k in range(9):
            
            ls.append(li[i]);
            i = i+1
        matrix.append(ls)
    for i in range(9):
        if "." not in matrix[i]:
            flag = True
    if flag:
        print("Given sudoku is solved")