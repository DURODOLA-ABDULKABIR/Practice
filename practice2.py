# while True:
#     line = input('> ')
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num > largest_so_far :
#       largest_so_far = the_num
#    print(largest_so_far, the_num)
# print('After', largest_so_far)

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [9, 41, 12, 3, 74, 15] :
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count, sum, sum / count)

# count = 0
# sum = 0
# print('Before', count, sum)
# for value in [9, 41, 12, 3, 74, 15] :
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# average = sum/count
# print('After', count, sum, average)

# def thing():
#     print('Hello')
#     print('Fun')
# thing()

# x = 5
# print('Hello')


# x = 5
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
# print('Yo')
# x = x + 2
# print(x)
# print_lyrics()


# def addtwo(a, b):
#     added = a + b
#     return added
# x = addtwo(3, 5)
# print(x)


# x = int(input ('enter a number; '))
# y = int(input ('enter a number; '))
# z = int(input ('enter a number; '))
# number = 0
# for largest_number in ( x, y, z):
#     if (largest_number > number):
#         number = largest_number
#         print (largest_number)


# smallest_number = None
# for value in [9, 12, 41, 3, 31, 90]:
#     if smallest_number is None:
#         smallsest_number = value
#     elif value < smallest_number:
#         smallest_number = value
#     print (smallest_number, value)


# smallest = None
# print('Before')
# for value in [9, 41, 12, 3, 74, 15] :
#     if smallest is None : 
#         smallest = value
#     elif value < smallest : 
#         smallest = value
#     print(smallest, value)
# print('After', smallest)


# x = int (input('enter a number here> '))
# y = int (input ('enter a numter here> '))
# z = int (input ('enter a number here> '))
# largest = None
# for num in [x, y, z]:
#     if largest is None:
#         largest = num
#     elif num > largest:
#         largest = num
# print ('largest number is', largest)


# def lyrics ():
#     print('I am in love with you ' +
#     'from the first day that I met you')
#     print ('you are the best thing that has ever happened to me')
# lyrics()


# ARITHMETIC PROGRESSION
# a = input ('enter the first term; ')
# try:
#     a = int(a)
# except:
#     print ('pls enter an integer value ')
#     exit ()
# d = input ('enter the common diff; ')
# try:
#     d = int(d)
# except:
#     print ('pls enter an integer value ')
#     exit()
# n = input ('enter number of terms; ')
# try:
#     n = int(n)
# except:
#     print ('pls enter an integer value ')
#     exit()
# x = -1
# y = 0
# z = 1
# while (n > 0):
#     term = a + ((x+z) * d)
#     y = y + 1
#     z = z + 1
#     print (term)
#     if (y == n) :
#         break
# print ('done!')
        

# SUM OF GP
a = input ('enter the 1st term; ')
try:
    a = int(a)
except:
    print ('please enter an integer value; ')
    exit()
b = input ('enter the 2nd term; ')
try: 
    b = int (b)
except:
    print ('please enter an integer value')
    exit()
n = input ('enter number of terms; ')
try: 
    n = int(n)
except:
    print ('please enter an integer value')
    exit()
r = a/b
if r > 1:
    s = a(r**n-1)/(r-1)
else:
    s = a(1-r**n)/(1-r)
print (s)






    

