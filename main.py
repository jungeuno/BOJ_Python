n = int(input())
l = []
l_new = []
for i in range(n):
  num = int(input())
  if num >= int(l[i]):
    l[i+1].append(num)
  else:
    temp = int(l[i])
    l[i].append(num)
    l[i+1].append(temp)
for i in l:
  print(i)