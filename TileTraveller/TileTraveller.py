#1. Fannst auðveldara að nota föllin, mögulega því þá var ég nánast bara að endurraða sama kóða og ég notaði í hinu.
#2. Það er mun læsilegra að nota föll, maður þarf í raun ekki að lesa föllin sjálf bara að sjá hvað þau gera.
#3. Aðalforritið er ekki jafn langt og það voru nokkrir hlutir sem ég þurfti að skrifa nokkrum sinnum 
# sem ég gat skrifað bara 1x í þessari útfærslu.
#https://github.com/matthildurfrida/verkefni/tree/master/TileTraveller
def possible_directions(x,y):
    '''All possible directions in each tile'''
    if x == 1 and y == 1:
        directions = N + "."
    elif x == 1 and y == 2:
        directions = N + " or " + E + " or " + S + "."
    elif x == 1 and y == 3:
        directions = E + " or " + S +"."
    elif x == 2 and y == 1:
        directions = N + "."
    elif x == 2 and y == 2:
        directions = S + " or " + W + "."
    elif x == 2 and y == 3:
        directions = E + " or " +  W + "."
    elif x == 3 and y == 2:
        directions = N + " or " + S + "."
    elif x == 3 and y ==  3:
        directions = S + " or " + W + "."
    return directions
    
def move_y(y):
    '''Changes the value of y'''
    if choice == "N":
        y +=1
    elif choice == "S":
        y-=1
    return y

def move_x(x):
    '''Changes the value of x'''
    if choice == "W":
        x -= 1
    elif choice == "E":
        x += 1
    return x

def choice_upper(choice):
    '''Makes users input uppercase'''
    choice = choice.upper()
    return choice

x = 1
y = 1
N = "(N)orth"
S = "(S)outh"
W = "(W)est"
E = "(E)ast"

is_valid_move = True
while True:
    directions = possible_directions(x,y)
    if is_valid_move:
        print("You can travel: " + directions)
    choice = choice_upper(input("Direction: ")) 
    if choice in directions:
        is_valid_move = True
        y = move_y(y)
        x = move_x(x)
    else:
        is_valid_move = False
        print("Not a valid direction!")
    if x == 3 and y == 1:
        print("Victory!")
        break


