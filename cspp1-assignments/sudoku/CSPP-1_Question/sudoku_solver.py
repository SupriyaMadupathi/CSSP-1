sudoku = input()
if len(sudoku) != 81:
 	print("Invalid Input")
elif '.' not in sudoku:
 	print("Given sudoku is solved")
else:
 	grid = list(sudoku)
 	list1 = []
 	list2 = []
 	count = 0
 	for i in range(len(list1)):
 		count[i] += 1
 		if count[1] == 2:
 			print("Invalid Sudoku:Duplicate values")
