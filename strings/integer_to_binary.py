my_int = int(input('Give me an int >= 0: '))

bstr = ""
quotient = my_int

while quotient > 0:
    remainder = quotient%2
    quotient = quotient//2
    bstr += str(remainder)
if my_int == 0:
    bstr = "0"

print("The binary of", my_int, "is", bstr[::-1])