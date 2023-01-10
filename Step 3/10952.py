total = []
while True:
  a,b = map(int, input().split())
  if a==0 and b==0:
    break
  total.append(a+b)
for i in range(len(total)):
  print(total[i])
