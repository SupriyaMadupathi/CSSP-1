'''
@ author SupriyaMadupathi
'''
def tic_tac_input():
    '''
    reads input
    '''
    input_matrix = []
    for _ in range(3):
        temp_list = input().split(" ")
        input_matrix.append(temp_list)
    return input_matrix
def input_validation(matrix):
    '''
    checking the input
    '''
    for i in matrix:
        for j in i:
            if j not in "x.o":
                return False
    return True
def start_game(matrix, winner_variable):
    '''
    start the game
    '''
    for row in matrix:
        if len(set(row)) == 1 and row[0] == winner_variable:
            return True
    return False

def new_transpose(matrix, increment, temp_matrix=[]):
    '''
    transpose of matrix
    '''
    if increment == len(matrix):
        return temp_matrix
    else:
        temp_matrix.append([matrix[0][increment], matrix[1][increment], matrix[2][increment]])
        return new_transpose(matrix, increment+1, temp_matrix)
def decide_winner(matrix, winner_variable):
    '''
    checking the input
    '''
    transpose_matrix = new_transpose(matrix, 0, [])
    if start_game(matrix, winner_variable) or\
    start_game(transpose_matrix, winner_variable) or\
    matrix[0][0] == matrix[1][1] == matrix[2][2] == winner_variable or\
    matrix[2][0] == matrix[1][1] == matrix[0][2] == winner_variable:
        return True
    return False
def invalid_game(matrix):
    '''
    checking the validation of game
    '''
    count_x = 0
    count_o = 0
    for column in matrix:
        count_x += column.count('x')
        count_o += column.count('o')
    if  count_o > 5 or count_x > 5 or count_x == count_o:
        return False
    return True

def main():
    '''
    main function
    '''
    matrix = tic_tac_input()
    #print(input_validation(matrix))
    if input_validation(matrix):
        if invalid_game(matrix):
            if decide_winner(matrix, 'x'):
                print('x')
            elif decide_winner(matrix, 'o'):
                print('o')
            else:
                print('draw')
        else:
            print("invalid game")
    else:
        print("invalid input")

if __name__ == '__main__':
    main()
