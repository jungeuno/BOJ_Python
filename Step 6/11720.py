n = int(input())
l = [int(input()) for i in range(n)]

result = 0
while l/10 >= 0:
  result += l%10
  