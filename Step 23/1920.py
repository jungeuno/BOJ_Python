N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

start = 0
mid = N//2
end = N

def binary_search(array1, array2, start, end):
  while start <= end:
    for i in range(start, mid):
      if array1[i] in array2:
        print(1)
      else:
        break
    mid = end
    start = (mid)+1
        
    