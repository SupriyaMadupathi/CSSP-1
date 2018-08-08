'''
#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some 
numbers in the tuple as input and returns a tuple in which 
contains odd index values in the input tuple
@ author SupriyaMadupathi
'''  



def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.s
    '''
    # Your Code Here
    nT = ()
    j = 0
    for i in aTup:
        if j % 2 == 0:
            nT = nT + (i,)
        j += 1
    return nT

def main():     
    '''     odd tuple      '''
    data = input()
    data =data.split()
    aTup=()     
    for j in range(len(data)):
       aTup +=((data[j]),)
    print(oddTuples(aTup))
if __name__ == "__main__":
    main()