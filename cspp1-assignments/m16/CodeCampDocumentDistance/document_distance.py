'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def combine_dict(word_one, word_two):
    '''returns dictionary
    '''
    dictionary = {}
    for word in word_one:
        if word in word_two:
            dictionary[word] = [word_one[word], word_two[word]]

    for word in word_one:
        if word not in dictionary:
            dictionary[word] = [word_one[word], 0]
    for word in word_two:
        if word not in dictionary:
            dictionary[word] = [0, word_two[word]]
    return dictionary
def calculate_similarity(dictionary):
    '''
    calculating frequency
    '''
    numerator = sum([k[0] * k[1] for k in dictionary.values()])
    dinominator_one = math.sqrt(sum([k[0] ** 2 for k in dictionary.values()]))
    dinominator_two = math.sqrt(sum([k[1] ** 2 for k in dictionary.values()]))
    return numerator/(dinominator_one*dinominator_two)

def create_dict_of_values(words_list):
    '''
    removing the spaces
    '''
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

def clean_up_words(word_input):
    '''
    cleaning the given words
    '''
    given_words = word_input.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", given_words).split(" ")
    return words

def similarity(word_one, word_two):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary_one = create_dict_of_values(clean_up_words(word_one))
    dictionary_two = create_dict_of_values(clean_up_words(word_two))
    #print(dictionary_one)
    #print(dictionary_two)
    dictionary = combine_dict(dictionary_one, dictionary_two)
    #print(dictionary)
    return calculate_similarity(dictionary)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename_:
        for line in filename_:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
