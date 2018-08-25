'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
    remove special characters
    '''
    word = ""
    regex = re.compile('[^a-zA-Z0-9]')
    clean_words = regex.sub("", word.strip()) 
    for word in string.lower():
        return clean_words

def main():
    '''
    string
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
