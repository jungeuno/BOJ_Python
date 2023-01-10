n = int(input())
l = (list(map(int, input().split())) for i in range(n))
v = int(input())
print(l.count(v))