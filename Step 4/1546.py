N = int(input())
score = [int(input()) for i in range(N)]
M = max(score)
set_score = []
for i in score:
  set_score.append(i/M*100)
print(sum(set_score)/N)