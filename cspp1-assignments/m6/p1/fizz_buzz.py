'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
@ author : SupriyaMadupathi
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    var = int(input())
    for i in range(0, var+1, 1):
        if i % 3 == 0 and  i % 5 == 0:
            print("Fizz")
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
if __name__ == "__main__":
    main()
