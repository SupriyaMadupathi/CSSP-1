'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList
 = [1, -4, 8, -9] into [1, 4, 8, 9]
 @ author SupriyaMadupathi
 '''


def apply_to_each(L, f):
    '''
   negative to positive
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
    print (L)

def main():
    '''
    negative to positive
    '''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()

