N = int(input())
s=[] #시작 시간
e=[] #종료 시간
l=[] #총 배열
for i in range(N):
  start, end = list(map(int, input().split()))
  s.append(s)
  e.append(e)
  l[i][0].append(start)
  l[i][1].append(end)
  l[i][2].append(start-end)

cnt = 1
e.sort()
for i in range(N):
  t = l[0][1]
  if l[i][0] >= t:
    cnt += 1
    t = l[i][1]
print(cnt)