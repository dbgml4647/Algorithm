# 40

#놀이기구 타기

limit_weight  =int(input())
sum_people = int(input())
people = []
#sort_people =[]
sumofweight =0

for i in range(0, sum_people):
  weight = int(input())
  people.append(weight)
  

#people.sort(reverse=True)
#print(people)

for i in range(0,sum_people):
  sumofweight = sumofweight + people[i]
  if sumofweight > limit_weight:
     print("총", i, "명이 탈 수 있습니다")
     break;

#print(people)
