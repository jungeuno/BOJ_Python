n = int(input())
result = []
r = 0
for i in range(n):
  answer = input()
  if answer[i] == 'X':
    r += 0
  elif answer[i] == answer[i-1]:
    r += i+1
  else:
    r += 1
  result.append(r)

for i in result:
  print(i)