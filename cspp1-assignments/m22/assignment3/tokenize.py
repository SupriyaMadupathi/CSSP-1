'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string, input1):
    '''
    tokenize the string
    '''
    dictionary = {}
    keys = string.split()
    for key in keys:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1

    return dictionary
def main():
    '''
    main function
    '''
    input_given = int(input())
    input_str = input()
    text = ''.join(input_str)
    text.split()
    print(tokenize(text, input_given))
if __name__ == '__main__':
    main()
