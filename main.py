n = int(input())
word = [input() for i in range(n)]

set_word = set(word)
word = list(set_word)
word.sort()
word.sort(key = len)

for i in word:
  print(i)