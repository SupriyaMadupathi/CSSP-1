'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
@ author supriyaMadupathi
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_2 = ""
    for char in  str_input:
        if char in "!@#$%^&*":
            str_2 += " "
        else:
            str_2 += char
    print(str_2)
if __name__ == "__main__":
    main()
