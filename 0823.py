# 41

number = int (input())
#print(number)
sum = 0 

for i in range(1,number):
  if(number % i==0):
      sum = sum + 1

#print(sum)
if ( sum < 2):
  print("YES")
else:
  print("NO")


#gggg