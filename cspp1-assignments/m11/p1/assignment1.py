'''
Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score for a single word. The function get_word_score should accept as input a string of lowercase letters (a word) and return the integer score for that word, using the game's scoring rules.
'''

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    


def get_word_score(word_1, n_1):
    """string"""
    
    sum_1 = 0
    dictionary_ = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    length_1 = len(word_1)
    
    for i in word_1:
        if i in dictionary_.keys():
            sum_1 = sum_1 + dictionary_[i]
    sum_1 = sum_1*length_1
    if n_1 == length_1:
        sum_1 += 50
    return sum_1

def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split(" ")
    print(get_word_score(data[0], int(data[1])))
if __name__ == "__main__":
    main()
