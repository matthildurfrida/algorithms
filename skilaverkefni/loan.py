loan = float(input("Input the cost of the item in $: "))

if loan <= 1000:
    interest_rate = 0.015 
else:
    interest_rate= 0.02

max_monthly_payment = 50.0
total_interest_paid = 0
nr_month = 0

while loan > 50.0:
    nr_month += 1
    interest_paid = loan * interest_rate
    total_interest_paid += interest_paid
    loan = loan - max_monthly_payment + loan*interest_rate # remaining debt
    print("Month:" + " " + str(round(nr_month,2)) + " Payment:" + " " \
     + str(round(max_monthly_payment,2)) + " Interest paid:" + " " + str(round(interest_paid,2))\
     + " Remaining debt:" + " " + str(round(loan,2)))
else: 
    nr_month += 1
    interest_paid = loan * interest_rate
    total_interest_paid += interest_paid
    rest_of_payment = loan 
    remaining_debt = loan - rest_of_payment + loan*interest_rate
    if remaining_debt < 1:
        rest_of_payment += interest_paid
        remaining_debt = 0.0
        print("Month:" + " " + str(round(nr_month,2)) + " Payment:" + " " \
        + str(round(rest_of_payment,2)) + " Interest paid:" + " " + str(round(interest_paid,2))\
        + " Remaining debt:" + " " + str(round(remaining_debt,2)))

print()
print("Number of months:" + " " + str(nr_month))
print("Total interest paid:" + " " + str(round(total_interest_paid,2)))