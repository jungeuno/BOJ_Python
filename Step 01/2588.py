a = int(input())
b = int(input())

x = b%10           #a의 1의 자리
y = (b//10)%10     #a의 10의 자리
z = (b//10)//10    #a의 100의 자리

print(x*a)
print(y*a)
print(z*a)
print(a*b)