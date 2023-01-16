n = int(input())
result = 0
cnt = 0

for i in range(1, n+1):
  answer = list(map(str, input().split()))
  if answer[i] == 'O':
    cnt += 1
    result += cnt
    if answer[i] == answer[i-1]:
      cnt += 1
  else:
    cnt = 0
  result += cnt
  
print(result)