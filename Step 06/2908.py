a, b = map(int, input().split())

re_a = []
re_b = []

for i in range(3):
  re_a.append(a%10)
  re_b.append(b%10)
  a = a//10
  b = b//10

if re_a > re_b:
  for i in re_a:
    print(i,end='')
else:
  for i in re_b:
    print(i,end='')