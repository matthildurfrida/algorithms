#Höfum upphafspunktinn x = 1 og y = 1. Skilgreinum hvaða áttir er hægt að fara í úr hverjum punkti.
#Leyfum notanda að velja átt, þegar hann velur áttina breytast gildi x eða y. y+=1 ef N, y-=1 ef S, x+=1 ef E og x-=1 ef W
#Ef notandinn velur átt sem er ekki í skilgreind í punktinum prentast villuboð og hann fær að slá inn nýja átt°


x = 1
y = 1
N = "(N)orth"
S = "(S)outh"
W = "(W)est"
E = "(E)ast"
 
is_valid_move = True
while True:
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
    if x == 3 and y == 1:
        print("Victory!")
        break
    if is_valid_move:
        print("You can travel: " + directions) 
    choice = input("Direction: ") 
    choice = choice.upper()
    if choice == "N" and N in directions:
        y +=1
        is_valid_move = True
    elif choice == "S" and S in directions:
        y-=1
        is_valid_move = True
    elif choice == "W" and W in directions:
        x -= 1
        is_valid_move = True
    elif choice == "E" and E in directions:
        x += 1
        is_valid_move = True
    else:
        print("Not a valid direction!")
        is_valid_move = False