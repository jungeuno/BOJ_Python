n = int(input())

if n < 10:
  n = n * 10

x = n//10
y = n%10
z = x+y
new = (y*10)+z
cycle = 1

if new == n:
  print(cycle)
  
while new == n:
  