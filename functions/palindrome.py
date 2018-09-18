import string
def palindrome(sentence):
    sentence_lower = sentence.lower()
    bad_characters = string.punctuation + string.whitespace
    good_characters = ""
    for character in sentence_lower:
        if character not in bad_characters:
            good_characters += character
    if   good_characters == good_characters[::-1]:
        return '"' + sentence + '"' + " is a palindrome."
    else:
        return '"' + sentence + '"' + " is not a palindrome."

in_str = input("Enter a string: ")

result = palindrome(in_str)
print(result)