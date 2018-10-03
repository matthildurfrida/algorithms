import random
import string

def get_word_string(text_file):
    '''Opens the textfile if the users input is right'''
    word_string = ""
    try:
        with open(filename,"r") as text_file:
            for line in text_file:
                word_string += line
    except FileNotFoundError:
        print("File", filename,"not found")
    return word_string

def scramble_string(word_string):
    '''Scrambles all letters in a word except the first and last and makes a new sentence'''
    word_list = word_string.split()
    new_list = []
    for word in word_list:
        if len(word.strip(string.punctuation)) < 3:
            new_word = word + " "
        else:
            word = list(word)
            first_l = word[0]
            last_l = word[-1]
            if last_l in string.punctuation:
                last_l = word[-2:]
            start = 1
            stop = -1
            if word[stop] in string.punctuation:
                stop -= 1 
            letters_to_scramble = word[start:stop]
            random.shuffle(letters_to_scramble)
            new_word = first_l + "".join(letters_to_scramble) + "".join(last_l) + " "
        new_list.append(new_word)
    scrambled_sentence = "".join(new_list)
    return scrambled_sentence

#Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)