'''# Exercise: fourth power

# Write a Python function, fourthPower, that takes in one number
 and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier
 exercise exercise (you don't need to redefine square in this box;

# This function takes in one number and returns one number.
@ author SupriyaMadupathi
'''

def square(x_s):
    '''
   fourth power
    '''
    # Your code here
    return x_s**2
def fourthpower(x_s):

    '''
   fourth power
    '''
    # Your code here
    return square(square(x_s))
def main():
    '''
    quaratic equation
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthpower(int(float(str(data)))))
    else:
        print(fourthpower(data))

if __name__ == "__main__":
    main()
