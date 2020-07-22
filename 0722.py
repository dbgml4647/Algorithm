#30 Return Index

text = input()
find = input() 


for i in range(len(text)):
  if (text[i] == find[0]):
    print(i)
    break


