'''
Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
@ author :SupriyaMadupathi
'''
def main():
    '''
    Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
'''

    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
    c_n = int(input())
    epsilon = 0.01
    step = 1
    g_a = 0
    while g_a <= c_n:
        if abs(g_a**3 - c_n) < epsilon:
            break
        else:
            g_a += step
    if abs(g_a**3 - c_n) >= epsilon:
        print(str(c_n) + "is not a perfect cube")
    else:
        print(str(c_n) + "is a perfect cube")


if __name__ == "__main__":
    main()
