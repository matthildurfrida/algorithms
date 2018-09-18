def find_new_position(starting_position):
    if choice == "r":
        if starting_position == END:
            new_position = starting_position
        else:
            new_position = starting_position + 1
    elif choice == "l":
        if starting_position == START:
            new_position = starting_position
        else:
            new_position = starting_position - 1
    else:
        new_position = starting_position
    return  "New position is: " + str(new_position)

def new_starting_position(starting_position,choice):
    if choice == "r":
        if starting_position < END:
            starting_position = starting_position + 1
    elif choice == "l":
        if starting_position > START:
            starting_position = starting_position - 1
    else:
        starting_position = starting_position
    return starting_position
        
START = 1
END = 10 
starting_position = int(input("Input a position between " + str(START) + " and " + str(END)+ ": "))

while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    choice = input("Input your choice: ")
    new_position = find_new_position(starting_position)
    print(new_position)
    starting_position = new_starting_position(starting_position,choice)
    if choice != "r" and choice != "l":
        break