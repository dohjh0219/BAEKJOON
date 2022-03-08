import sys
from types import LambdaType

input=sys.stdin.readline

n=int(input())

user=[]

for i in range(n):
    user.append(list(input().split()))

user.sort(key=lambda a:int(a[0])) ## age만 분석하여 sort함.

for i in range(n):
    print(user[i][0], user[i][1])