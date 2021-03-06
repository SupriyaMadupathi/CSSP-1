
def main():
    n = int(input())
    for i in range(n):
        value = int(input())
        happyNumber(value)

def happyNumber(value):
    result = False
    prevSums = []
    while not(result) and value not in prevSums:
        prevSums.append(int(value))
        sum = 0
        #print(prevSums)
        while int(value) > 0:
            sum += pow(int(value) % 10, 2)
            value = int(value) / 10
        if sum == 1:
            result = True
        else:
            value = sum
    if(result):
        print("Happy Number")
    else:
        print("Not a Happy Number")
main()
