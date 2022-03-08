import sys
from types import LambdaType

input=sys.stdin.readline

n=int(input())

user=[]

for i in range(n):
    user.append(list(input().split()))

user.sort(key=lambda a:int(a[0]))

for i in range(n):
    print(user[i][0], user[i][1])