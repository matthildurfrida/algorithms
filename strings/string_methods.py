name = input("Input a name: ")
index_of_comma = -1
for index, letter in enumerate(name):
    if letter == ",":
        index_of_comma = index


last_name = name[0:index_of_comma]
first_initial = name[index_of_comma+2:index_of_comma+3]

print(first_initial.capitalize() + ".", last_name.capitalize())