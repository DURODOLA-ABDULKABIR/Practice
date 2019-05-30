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

while True:
    line = input ('> ')
    if len(line) > 0 and line[0] == '#':
        # or 
    # if line.startswith ('#'): #to avoid error when there is no input by the user
        continue
    if line == 'done':
        break
    print (line)
print ('done!')
