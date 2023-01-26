N = int(input())
words = [input() for i in range(N)]
cnt = 0

for word in words:
  for w in word:
    