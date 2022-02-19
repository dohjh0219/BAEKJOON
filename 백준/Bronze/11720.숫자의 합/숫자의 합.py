N=int(input())

num=list(map(int,input()))
sum=0

for i in range(1,N+1):
    sum=sum+num[i-1]

print(sum)