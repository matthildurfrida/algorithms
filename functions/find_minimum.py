def find_min(a,b):
    if a < b:
        return a
    else:
        return b

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
minimum = find_min(first,second)
print("Minimum: ", minimum)