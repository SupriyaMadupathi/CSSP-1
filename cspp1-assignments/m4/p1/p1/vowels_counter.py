'''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels
 are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
@ author :SupriyaMadupathi
'''

def main():
    '''
    #Assume s is a string of lower case characters.
    Write a program that counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
    '''
     str_input = input()
    num_vow = 0
    for char in str_input:
        if char in "aueoi":
            num_vow += 1
    print(num_vow)

if __name__ == "__main__":
    main()
