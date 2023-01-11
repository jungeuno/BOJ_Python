n = int(input())
word = [input() for i in range(n)]
l = []
for i in word:
  if len(i) > len(i+1):
    l.append(i+1)
    l.append(i)
  else:
    l.append(i)
    l.append(i+1)

for i in word:
  print(i)