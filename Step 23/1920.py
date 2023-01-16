N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

start = 0
mid = N//2
end = N

def binary_search():
  while start <= end:
    