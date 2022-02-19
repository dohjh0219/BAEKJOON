n,x=map(int,input().split())

a=list(map(int,input().split()))

for i in range(1,int(n)+1):
    if a[i-1]<x:
        print(a[i-1],end=' ')