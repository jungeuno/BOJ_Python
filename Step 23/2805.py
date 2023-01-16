N, M = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = len(height)

while start <= end:  
  total = 0
  mid = (start + end)//2
  for i in range(start, end):
    total += height[i] - height[mid]
    if total < M:
      end = mid-1
    else:
      start = mid+1
            
print(mid)