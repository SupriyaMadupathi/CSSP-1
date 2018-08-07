'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number 
and returns the sum of digits of given number.

# This function takes in one number and returns one number.
@ author : SupriyaMadupathi
'''


def sumofdigits(n_a):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_a == 1:
        return 1
    else:
        return n_a * sumofdigits(n_a)

def main():
    '''
    sum of digits
    '''
    n_a = input()
    print(sumofdigits(int(n_a)))

if __name__ == "__main__":
    main()

