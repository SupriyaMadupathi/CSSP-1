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
    e_b = 0.01
    s_c = 0.1
    g_y = 0.0
    while abs(g_y **2-a_i) >= e_b:
        if g_y <= a_i:
            g_y += s_c
        else:
            break
    if abs(g_y**2 - a_i) >= e_b:
        print("failed")
    else:
        print(str(g_y))
    # epsilon and step are initialized
    # don't change these values
    # your code starts here

if __name__ == "__main__":
    main()
