# Assignment-3
'''
At this point, we have written code to generate a random hand and display 
that hand to the user. We can also ask the user for a word (Python's input) 
and score the word (using your getWordScore). However, at this point we have
 not written any code to verify that a word given by a player obeys the rules 
 of the game. A valid word is in the word list; and it is composed entirely of letters
  from the current hand. Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you will want 
to test your implementation by calling it multiple times on the same hand - what 

should the correct behavior be? Additionally, the empty string ('') is not a valid 
word - if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate 
tests in test_ps4a.py before pasting your function definition here.
@ author SupriyaMadupathi
'''
def is_valid_word(word_1, hand_1, word_list):
    """string"""
    if word_1 not in word_list:
        return False
    for i_1 in word_1:
        if i_1 not in hand_1.keys():
            return False
    return True
def main():
    """string"""
    word_1 = input()
    n_1 = int(input())
    adict_1 = {}
    for i in range(n_1):
        data = input()
        i = i+1
        i = i-1
        l_1 = data.split()
        adict_1[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_valid_word(word_1, adict_1, l_2))
if __name__ == "__main__":
    main()


