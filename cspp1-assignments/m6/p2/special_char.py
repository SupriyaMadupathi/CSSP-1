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
    s = "$upr!y@"
    for char in range (s):
        if char in "!@#$%^&*":
            print(" ")
    print(s)
if __name__ == "__main__":
    main()
