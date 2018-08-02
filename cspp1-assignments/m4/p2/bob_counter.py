'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
@ author SupriyaMadupathi
'''

def main():
    '''
    Assume s is a string of lower case characters.

    Write a program that prints the number of times the string 'bob' occurs in s.
    '''
    str_input1 = input()
    sub_input2 = "bob"
    count = 0
    flag = 1
    start = 0
    while flag:
        a_i = str_input1.find(sub_input2, start)
        if a_i == -1:
            flag = 0
        else:
            count += 1
            start = a_i+1
    print(count)

if __name__ == "__main__":
    main()
