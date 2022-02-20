n=int(input())

data=[]
count=[1]*n

for i in range(0,n):
    data.append(list(map(int,input().split())))
    
for j in range(0,n):
    for k in range(0,n):
        if data[j][0]<data[k][0] and data[j][1]<data[k][1]:
            count[j]+=1

for s in range(0,n):
    print(count[s],end=' ')