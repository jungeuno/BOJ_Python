s = input()
l = list(range(ord('a'), ord('z')+1))

for i in l:
  print(s.find(chr(i)), end=' ')