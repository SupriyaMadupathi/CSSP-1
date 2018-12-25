sudoku = input()
if len(sudoku) != 81:
    print("Invalid input")
elif '.' not in sudoku:
    print("Given sudoku is solved")
else:
    grid = list(sudoku)
    list1 = []
    list2 = []
    print(grid)
    for i in range(len(grid)):
        print(grid)
        list1.append(grid)
        print(list1)
        #for i in list1:
        #   count[i] += 1
         #  if count[1] == 2:
          #     print("Invalid Sudoku:Duplicate values")
