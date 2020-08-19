# 38

grade = input().split(' ')
grade.sort()


long = len(grade)
first = grade.count(grade[0])
secondIndex = long-first -1
second = grade.count(grade[secondIndex])

thirdIndex = secondIndex-second
third = grade.count(grade[thirdIndex])

print(first+second+third)