hour = int(input())
min = int(input())

if min-45>=0:
  print(hour,min-45)
else:
  if hour-1>=0:
    print(hour-1,min+15)
  else:
    print(23, min+15)
    