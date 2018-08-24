def mult_matrix(m_one, m_two):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(m_one)
    columns = len(m_two[0])
    multiplication_result = generate_matrix(rows, columns)
    if len(m_one[0]) == len(m_two):
        for i in range(len(m_one)):
            for j in range(len(m_two[0])):
                for k in range(len(m_two)):
                    multiplication_result += m_one[i][j] * m_two[i][j]
                    return multiplication_result


def generate_matrix(rows, columns):
    add_matrix = [[0 for i in range(columns)] for j in range(rows)]
    return add_matrix  

def add_matrix(m_one, m_two):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    rows = len(m_one)
    columns = len(m_one[0])
    add_matrix = generate_matrix(rows, columns)
    if len(m_one[0]) == len(m_two[0]):
        for i in range(len()):
            for j in range(columns):
                add_matrix[i][j] += m_one[i][j] + m_two[i][j]
                return add_matrix
    else:
        print("Error: Invalid input for the matrix")
        return None 


    

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_of_input = input().split(",")
    rows,  columns = int(list_of_input[0]), int(list_of_input[1])
    for _ in range(rows):
        list_of_row = input().split()
        if columns == len(list_of_row):
            list_of_input.append()
        else:
            print("Error: Invalid input for the matrix")
        return None 
    return matrix  
def main():
    # read matrix 1
    m_one = read_matrix()
    if m_one is None:
        exit()
    # read matrix 2
    m_two = read_matrix()
    if m_two is None:
        exit()

    # add matrix 1 and matrix 2
    print(add_matrix(m_one, m_two))


    # multiply matrix 1 and matrix 2
    print(mult_matrix(m_one, m_two))    

if __name__ == '__main__':
    main()
