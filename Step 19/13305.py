N = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.sort(reverse=True)
l = sum(lengths)
result = 0
if min(prices) == prices[0]:
  result += prices[0]*l
elif max(prices) == prices[0]:
  result += prices[0]*lengths[0]

  for i in range(1, N):
    result += lengths[i]*prices[i]
print(result)

  