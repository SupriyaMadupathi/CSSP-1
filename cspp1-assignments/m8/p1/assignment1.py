'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
 number and returns the factorial of given number.

# This function takes in one number and returns one number.
@ author : SupriyaMadupathi
'''


def factorial(n_a):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_a in (0, 1):
        return 1
    return n_a * factorial(n_a-1)

def main():
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    n_a = input()
    print(factorial(int(n_a)))

if __name__ == "__main__":
    main()
