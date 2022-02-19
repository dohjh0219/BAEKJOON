N=int(input())

data=list(map(int,input().split()))

new=max(data)
in_new=data.index(new)

for i in range(1,N+1):
    data[i-1]=data[i-1]/new*100

sum=0

for i in range(1,N+1):
    sum=sum+data[i-1]

print(sum/N)