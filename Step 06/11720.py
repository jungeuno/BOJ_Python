n = int(input())
l = str(input())
result = 0

for i in range(n):
  result += int(l[i:i+1])
print(result)