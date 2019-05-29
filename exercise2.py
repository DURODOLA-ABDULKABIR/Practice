hours = int(input ('hours worked; '))
rate = int(input ('please enter your rate; '))
overtime = (hours - 40)

if (hours > 40) and (hours > 60):
    hours = 60
    pay = hours *  rate
    print ('payment =', pay + (overtime * 1.5))
else:
    pay = hours *  rate
    print ('payment =', pay)
