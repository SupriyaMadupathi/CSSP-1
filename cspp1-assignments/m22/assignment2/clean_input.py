'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
    remove special characters
    '''
    string = ''
    words = re.sub('[^a-zA-Z0-9]', " ", string.lower().replace('\'', ''))
    #given_input = string.lower().strip
    #regex = re.compile('[a-zA-Z0-9]')
    #words = 
    return words    

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
