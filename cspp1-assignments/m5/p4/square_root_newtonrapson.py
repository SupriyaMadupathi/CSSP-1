'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
@ author : SupriyaMadupathi
'''
def main():
    '''
    # Write a python program to find the square root of the given number
    # using approximation method

    # testcase 1
    # input: 25
    # output: 4.999999999999998
    '''
    a_i = int(input())
    e_n = 0.01
    g_s = a_i/2.0
    while abs(g_s*g_s - a_i) >= e_n:
        g_s = g_s - (((g_s**2) - a_i)/(2*g_s))
    print(str(g_s))
    # epsilon and step are initialized
    # don't change these values
    # your code starts here

if __name__ == "__main__":
    main()
    