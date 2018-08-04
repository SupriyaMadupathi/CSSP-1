'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
    @ author SupriyaMadupathi
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    i_ = int(input())
    p_ = 1
    while i_ > 0:
        a_ = i % 10
        i_ = i // 10
        p_ = p*a
    print(p)
if __name__ == "__main__":
    main()
