N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

def find(array, i, target):
  
  if array[i] == target:
    return
    