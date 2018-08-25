'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    lines = int(input())
    for i in range(lines):
        i += 1
        lines = input()
    print(lines)

if __name__ == '__main__':
    main()
