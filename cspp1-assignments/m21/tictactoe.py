def tic_tac_input():
	input_matrix = []
	for i in range(3):
		temp_list = input().split(" ")
		input_matrix.append(temp_list)
	return input_matrix
def input_validation(matrix):
	for i in matrix:
		for j in i:
			if j not in "x.o":
				return False
	return True
def start_game(matrix):
	pass
def invalid_game(matrix):
	count_x = 0
	count_o = 0
	for column in matrix:
		count_x += column.count('x')
		count_o += column.count('o')
	if 	count_o > 5 or count_x > 5 or count_x == count_o:
		return False
	return True

def main():
	matrix = tic_tac_input()
	#print(input_validation(matrix))
	if not input_validation(matrix):
		print("invalid input")
	elif not invalid_game(matrix):
		print("invalid game")
	else:
		start_game(matrix)

if __name__ == '__main__':
    main()
