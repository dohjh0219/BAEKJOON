import sys

input=sys.stdin.readline

n=int(input())

array=[]

for i in range(n):
    array.append(list(map(int,input().split())))

s_array=sorted(array)

for i in range(n):
    print(s_array[i][0],s_array[i][1])