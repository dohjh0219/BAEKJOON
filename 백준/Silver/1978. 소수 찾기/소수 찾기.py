n=int(input())

data=list(map(int,input().split()))
result=[]

for i in data:
    count=0

    for k in range(2,i):
        if i%k==0:
            count+=1

    if i!=1:
        if count==0:
            result.append(i)

print(len(result))