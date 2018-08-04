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
    '''
    n_a = int(input())
    e_b = 0.01
    l_w = 0.0
    h_i = n_a
    m_i = (l_w + h_i)/2.0
    while abs(m_i**2-n_a) >= e_b:
        if m_i**2 < n_a:
            l_w = m_i
        else:
            h_i = m_i
        m_i = (l_w +h_i)/2.0
    print(m_i)
    # epsilon and step are initialized
    # don't change these values
        # your code starts here

if __name__ == "__main__":
    main()
