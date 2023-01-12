n = int(input())
l = []
for i in range(n):
  num = int(input())
  if num >= l[i]:
    l[i+1].append(num)
  else:
    temp = l[i]
    l[i].append(num)
    l[i+1].append(temp)
for i in l:
  print(i)