import string
def count_case(sentence):
    upper = 0
    lower = 0

    for character in sentence:
        if character in string.ascii_uppercase:
            upper += 1
        if character in string.ascii_lowercase:
            lower += 1
    return upper, lower

user_input = input("Enter a string: ")

upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)