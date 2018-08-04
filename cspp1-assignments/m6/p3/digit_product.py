'''
Given a  number int_input, find the product of all the digits
example: input: 123
    output: 6
    @ author SupriyaMadupathi
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    i = int(input())
    produc_t = 1
    while i > 0:
        a_b = i % 10
        i = i // 10
        produc_t = produc_t*a_b
    print(produc_t)
if __name__ == "__main__":
    main()
