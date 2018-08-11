'''
#Exercise: Assignment-2
#Implement the updateHand function. Make sure this function has
no side effects: i.e., it must not mutate the hand passed in.
Before pasting your function definition here, be sure you've
passed the appropriate tests in test_ps4a.py.
@ author: SupriyaMadupathi
'''

def update_hand(hand_1, word_1):
    """a2"""
    hand_new = dict(hand_1)
    for i in word_1:
        if i in hand_1.keys():
            hand_new[i] = hand_new[i] - 1
    return hand_new
def main():
    """string"""
    n_1 = input()
    adict_1 = {}
    for i in range(int(n_1)):
        data = input()
        i = i
        l_1 = data.split(" ")
        adict_1[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict_1, data1))
if __name__ == "__main__":
    main()
