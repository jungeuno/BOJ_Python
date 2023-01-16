n = int(input())

for i in range(n):
  result = 0
  cnt = 0
  answer = list(input())
  for i in range(0, len(answer)):
    if answer[i] == 'O':
      cnt += 1
    else:
      cnt = 0
    result += cnt
  print(result)