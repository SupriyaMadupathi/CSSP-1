def check():
    values = input()
    l= []
    for i in values:
        l.append(i)
    matrix = []
        # matrix = [9][9]
    # print(l)
    i = 0
    flag = False
    for j in range(9):
        ls = []
        for k in range(9):
            # print(str(j)+" "+str(k))
            # for i in l:
            ls.append(l[i]);
            i=i+1
        matrix.append(ls)
    # print(matrix)
    for i in range(9):
        if "." not in matrix[i]:
            flag = True
    if flag:
        print("Given sudoku is solved")