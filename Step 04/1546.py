N = int(input())
score = list(map(int, input().split()))
M = max(score)
set_score = [i/M*100 for i in score]
print(sum(set_score)/N)