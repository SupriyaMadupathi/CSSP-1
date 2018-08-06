'''# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
 that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
@ author SupriyaMadupathi
'''


def evalquadratic(a_1, b_2, c_3, x_1):
    '''
    Quadratic equation
    '''
    z_s = (a_1 * (x_1**2) + (b_2*x_1) + c_3)
    return z_s
def main():
    '''
    Quadratic queation
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x_1 in range(len(data)):
        temp = str(data[x_1]).split('.')
        if temp[1] == '0':
            data[x_1] = int(float(str(data[x_1])))
        else:
            data[x_1] = data[x_1]
    print(evalquadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
