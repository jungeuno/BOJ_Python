N, K = map(int, input().split())

cnt1 = 0
cnt2 = 0
cnt3 = 0
for a in range(N):
  if a == K or a%10 == K or a//10 == K:
    cnt1 += 1
for b in range(60):
  if b == K or b%10 == K or b//10 == K:
    cnt2 += 1
for c in range(60):
  if c == K or c%10 == K or c//10 == K:
    cnt3 += 1

print(cnt1*cnt2*cnt3)