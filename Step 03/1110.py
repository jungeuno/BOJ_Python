'''N = int(input())
cycle = 0
tmp_n = N

while True:
    x = tmp_n//10
    y = tmp_n%10
    tmp_n = (y%10)+(x+y)
    cycle += 1
    if (tmp_n == N):
      break
      
print(cycle)'''
#######################################33
input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정 
print(cnt)