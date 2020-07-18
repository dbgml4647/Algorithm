#27 making a dictionary


dic = {}
name =[]
number = []

name = input()
number =input()

final_name = name.split(" ")
final_number = number.split(" ")

dic.update({final_name[0]:final_number[0]})
dic.update({final_name[1]:final_number[1]})

print(dic)
#Debug