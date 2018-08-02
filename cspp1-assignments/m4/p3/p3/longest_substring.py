'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the
 letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that
 you move on to a different part of the course.
If you have time, come back to this problem after
you've had a break and cleared your head.
@ author SupriyaMadupathi'''

def main():
    '''
    Assume s is a string of lower case characters.

    Write a program that prints the longest substring of s in which the
    letters occur in alphabetical order.
    For example, if s = 'azcbobobegghakl', then your program should print

    Longest substring in alphabetical order is: beggh
    '''
    input_st = input()
    a_st = ""
    for i in range(len(input_st)-1):
        sub_st = input_st[i]
        while i+1 < len(input_st) and input_st[i] <= input_st[i+1]:
            i += 1
            sub_st += input_st[i]
        if len(sub_st) > len(a_st):
            a_st = sub_st
    print(a_st)

if __name__ == "__main__":
    main()
