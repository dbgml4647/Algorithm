#Sort Pring
o_list = []
s_list = []
o_list = input().split(' ')

s_list = sorted(o_list)

if( o_list == s_list):
  print("YES")
else:
  print("NO")
