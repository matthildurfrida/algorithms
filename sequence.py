n = int(input("Enter the length of the sequence: "))

the_sum = 0
int_1 = 1
int_2 = 2
int_3 = 3

print(int_1)
print(int_2)
print(int_3)

for n in range(4,n+1):
    the_sum = int_1 + int_2 + int_3
    print(the_sum)
    int_1 = int_2 
    int_2 = int_3
    int_3 = the_sum
#g