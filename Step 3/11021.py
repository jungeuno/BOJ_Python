T = int(input())

sum=[]
for i in range(1, T+1):
  a,b = map(int, input().split())
  sum.append(a+b)

for i in range(1, T+1):
  print(('Case #{0}: {1}').format(i, sum[i-1]))