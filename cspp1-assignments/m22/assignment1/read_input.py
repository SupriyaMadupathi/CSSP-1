'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    lines = int(input())
    for i in range(lines):
        lines = input()
        i += 1
    print(lines)

if __name__ == '__main__':
    main()
