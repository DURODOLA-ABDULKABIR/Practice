hours = int(input ('hours worked; '))
rate = int(input ('please enter your rate; '))
pay = hours *  rate
overtime = (hours - 40)
if (hours > 40):
    print ('payment =', pay + (overtime * 1.5))
else:
    print ('payment =', pay)
