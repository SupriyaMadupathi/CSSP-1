'''
# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.
@ author SupriyaMadupathi
'''

def square(x_1):
    '''
    find the square
    '''
    c_1 = x_1**2
    return c_1
def main():
    '''
    square of number
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
