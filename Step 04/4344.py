c = int(input())
for i in range(c):
  students = list(map(int, input().split()))
  total = 0
  cnt = 0
  for score in range(1, students[0]+1):
    total += students[score]
  avg = total/students[0]
  for s in range(1, students[0]+1):
    if students[s] > avg:
      cnt += 1
  print('{0:.3f}%'.format(cnt/students[0]*100))