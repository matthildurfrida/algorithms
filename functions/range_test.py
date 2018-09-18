def range_test(integer):
    if integer in range(2,555):
        return str(integer) + " is in range."
    else:
        return str(integer) + " is outside the range!"


num = int(input("Enter a number: "))

number = range_test(num)
print(number)