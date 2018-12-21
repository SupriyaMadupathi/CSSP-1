def assign(values, s, d):
    other_values = values[s].replace(d, '')
    print("Given sudoku is solved")
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

#def display(values):
def search(values):
    
        return False 
        if all(len(values[s]) == 1 for s in squares):
            return values
        n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
        return some(search(assign(values.copy(), s, d))
                for d in values[s])
def sudoku(arr):
    inp = int(input()).split()
    print(inp)
    for i in range(9):
        for j in range(9):
            print(arr[i][j])
        print("Given sudoku is solved")