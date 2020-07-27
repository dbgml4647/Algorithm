#33 Reverse print
list = []
ch = input()

list = ch.split(' ')
list.reverse()

for i in list:
  print(i, end=" ")
