R = input()
s = []
S_new = []

for i in range(R):
  cnt, S1 = input().split()
  cnt = int(cnt)
  s.append(S1)
  for i in range(len(S1)):
    S_new.append(s[i]*cnt)

for i in range(len(S_new)):
  print(i)