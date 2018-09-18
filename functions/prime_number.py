def prime_number(number):
    if number == 2:
        return str(number) + " is a prime"
    for i in range(2,number):
        if number%i == 0:
            return str(number) + " is not a prime"
    return str(number) + " is a prime"

            
num = int(input("Input an integer greater than 1: "))

result = prime_number(num)
print(result)
