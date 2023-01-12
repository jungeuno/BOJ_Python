T = int(input())

x = []
y = []
for i in range(T):
  a,b = map(int, input().split())
  x.append(a)
  y.append(b)

for i in range(T):
  print(('Case #{0}: {1} + {2} = {3}').format(i+1, x[i], y[i], x[i]+y[i]))