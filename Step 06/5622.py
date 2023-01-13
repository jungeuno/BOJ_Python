d = input()

dials = ['1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ','0']
cnt = 0

for i in range(len(d)):
  for dial in dials:
    if d[i] in dial:
      cnt += dials.index(dial)+1

print(cnt+len(d))