'''
#Exercise: Assignment-4
#We are now ready to begin writing the code that
interacts with the player. We'll be implementing the playHand function.
 This function allows the user to play out a single hand. First, though,
 you'll need to implement the helper calculateHandlen function,
 which can be done in under five lines of code.
@ author SupriyaMadupathi
'''

def calculate_hand_len(hand_1):
    """sum"""
    sum_1 = 0
    for i_1 in hand_1.keys():
        # print(i_1)
        sum_1 = sum_1 + hand_1[i_1]
        # print(hand_1[i_1])
    return sum_1
def main():
    """sum"""
    n_1 = int(input())
    adict = {}
    i_1 = 0
    #for i_1 in range(int(n_1)):
    while i_1 < n_1:
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
        i_1 += 1
    print(calculate_hand_len(adict))
if __name__ == "__main__":
    main()
