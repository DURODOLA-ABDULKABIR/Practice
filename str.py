# fruit = ('banana')
# letter = fruit[-6]
# print (letter)


# fruit = ('banana')
# index = 0
# while index < len(fruit):
#     letter = fruit [index]
#     print (index, letter)
#     index = index + 1

# WRITING BANANA BACKWARDS
# fruit = ('banana')
# index = 0
# while index < len(fruit):
#     letter = fruit[(index +1) - 6 ] #(starts printing letters from index = -1)
#     print(index, letter)
#     index = index + 1 


# fruit = ('banana')
# for hit in fruit:
#     print (hit)


# fruit = ('banana')
# flex = 0
# while flex < len(fruit):
#     letter = fruit[(flex +1) - 6 ] #(using another word instead of index)
#     print(flex, letter)
#     flex = flex + 1 

# fruit = ('banana')
# reverse = fruit[::-1]
# print (reverse)

# t = ('fruit')
# f = t[:1]
# print (f)

# fruit = ('banana')
# count = 0
# for letter in fruit:
#     if letter == 'n':
#         count = count + 1
#         print (count)

# def count():
#     fruit = input('enter the name of a fruit\n')
#     letter = input('which letter do you want to count?\n')
#     num = 0
#     for alphabet in fruit:
#         if letter == alphabet:
#             num = num + 1
#     return num
# print (count())            
    
# word = input('Enter your word here\n')
# if word < 'banana':
#     print ('your word ' + word + ' is before banana')
# elif word > 'banana':
#         print ('your word ' + word + ' is after banana')
# else: print('No comparism')

#I DON'T UNDERSTAND HOW 'while True' works
# heading = 'Have a nice day'
# if heading.startswith ('H'):
#     print ('ok')
# lower = heading.lower()
# print (lower)

#slicing a line of words
# mail = 'email is adeneeyee@gmail.com as submitted on 24 may 2019'
# find1 = mail.find('@')
# print (find1)
# find2 = mail.find (' ', find1)
# print (find2)
# mail_type = mail[find1 + 1 : find2]
# print (mail_type)

#the format operator % allows one to construct strings, replacing part of the string with data stored in a variable
#"%d formats integer", "%g formats floats", "%s formats stings"
# camels = 42
# result = '%d' %camels
# print ('I have spotted ' + result + ' camels')
# print (result)

# sentence = 'In my %d years in France, I have seen %g %s' %(4, 4.5,'comets')
# print (sentence)

# if len(line) > 0 and line[0] == '#':
#         # or 
#     # if line.startswith ('#'): #to avoid error when there is no input by the
#         continue
#     if liwhile True:
#     line = input ('> ')
#     ne == 'done':
#         break
#     print (line)
# print ('done!')

# add = 'X-DSPAM-cofidence:0.8475'
# place = add.find(':')
# print (place)
# ans = add[(17+1):]
# print (ans)
# convert = float(ans)
# print (convert)
# op = convert + 1
# print (op)

#LISTS
# LOOPING THROUGH A LIST
# words = ['hut', 'got', 'frog']
# digits = [3, 9, 13, 5, 54, 7]
# for i in range (len(digits)):
#     digits [i] = digits[i] * 2
# empty= []
# words [1] = 1 
# print(words, digits, empty)

# LIST OPERATIONS
# a = [1, 3, 5, 8]
# b = [9, 1, 4, 6]
# c = a + b
# print (c)
# d = a * 3 #repeats the list (a) three times
# print (d)

# # LIST SLICES IS THE SAME AS STRING SLICES

# #LIST METHODS
# a.append(9) #adds another element to the list
# print (a)
# b.extend(a) #adds list "a" to b
# print (b)
# b.sort() #arranges the new "b" from low to high
# print (b)
# # b = b.sort()
# # print (b) #list methods are void, they return none

# #DELETING ELEMENTS
# x = b.pop(2) #removes the element with index specified 
# print (b) #returns the rest
# print (x) #returns the element removed
# # y = b.pop() #no index specified, returns only the last element
# # print (b)
# # print (y)

# #If the removed value is not needed, use delete
# del b[1]
# print (b)
# # if the index of the element is not known use remove
# b.remove(9)
# print (b)
# # to remove more than one element
# del b[1:4]
# print (b)

# #LIST OPERATIONS
# print (len(b))
# print (sum(b))
# print (max(b))
# print (min(b))
# print (sum(b)/len(b))

#FINDING AVERAGE
# total = 0
# count = 0
# while True:
#     inp = input ('Enter a number:\n')
#     if inp == 'done':
#         break
#     try:
#         value = float (inp)
#     except:
#         print ('please enter an integer ')
#     total = total + value
#     count = count + 1
# average = total/count
# print ('Average', average)

#ALTERNATIVELY
# num_list = list()
# while True:
#     inp = input('Enter a number here:\n')
#     if inp == 'done':
#         break
#     try:
#         value = float (inp)
#     except:
#         print ("please enter an integer")
#     num_list.append(value)
# average = (sum(num_list)/len(num_list))
# print ('Average =', average)

#CONVERTING STTRING TO LIST
# s = ('pining for the fjords')
# t = s.split()
# d = t.pop(2)
# print (d)
# y = list(s)
# print ('here is split:', t)
# print ('here is list:', y)

#SPLITTING AND JOINING USING delimiter
# delimiter = ' '
# j = delimiter.join(t)
# delimiter = ''
# k = delimiter.join(y)
# print (j)
# print (k)

#parsing lines ( I don't understand line 219)
fhand = open('textdoc.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith ('The'):
        continue
    words = line.split()
    print (words[16])
