R = int(input())
l = []

for i in range(R):
  n, codes = input().split()
  n = int(n)
  for code in codes:
    print(code*n, end='')
  print()