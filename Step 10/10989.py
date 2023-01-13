n = int(input())
l = [int(input()) for i in range(n)]

for i in range(n):
  idx = i
  l.index(min(l)) 