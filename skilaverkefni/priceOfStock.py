def nr_shares_input():
    '''Checks if users input is correct'''
    while True:
        try: 
            nr_shares = input("Enter number of shares: ")
            int(nr_shares)
            break
        except ValueError:
            print("Invalid number!")
    return nr_shares

def price_input():
    '''Checks if users input is correct'''
    while True:
        try: 
            input_price = input("Enter price (dollars, numerator, denominator): ")
            price = input_price.replace(" ","")
            int(price)
            break
        except ValueError:
            print("Invalid price!")
    return input_price

def find_market_price():
    '''Takes input_price and finds market price'''
    dollars, numerator, denominator = input_price.split()  
    market_price = dollars + " " + numerator +"/" + denominator
    return market_price

def find_value():
    '''Calculates the value of shares'''
    dollars, numerator, denominator = input_price.split()
    value = float(nr_shares)*(float(dollars) + float(numerator)/float(denominator))
    return value

def continue_choice():
    '''Gives users the choice to continue or stop'''
    choice = input("Continue: ")
    return choice

def output():
    return print("{} shares with market price {} have value ${:.2f}".format(nr_shares, market_price, value))

choice = "y"
while choice == "y":
    nr_shares = nr_shares_input()
    input_price = price_input()
    market_price = find_market_price()
    value = find_value()
    output()
    choice = continue_choice()



    



        

    