# total = 0
# count = 0
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value     
#     count = count + 1

# average = total / count
# print('Average:', average)


# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)

# TO OPEN A FILE
# fhand = open('mbox-short.txt')
# for line in fhand:
#      line = line.rstrip()
#      if not line.startswith('From ') : continue
#      words = line.split()
#      print(words[2])


names = ['Tobi', 'Shola', 'is', 'Kola', 'for', 'while', 'Aisha', 'in']
functions = ['is', 'for', 'while', 'in']
for name in names:
    if name not in functions:
        print(name)



   