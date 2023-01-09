h,m = map(int, input().split())
t = int(input())

set_h = h+(t//60)
set_m = m+(t%60)
  
while set_m > 59:
  set_m = set_m%60
  set_h += 1
  
if set_h >= 24:
  set_h %= 24
  
print(set_h, set_m)