N,K = map(int, input().split())
l = [int(input()) for i in range(N)]
l.sort(reverse=True)
cnt = 0
for i in l:
  if i <= K:
    cnt += K//i
    K %= i
print(cnt)