c=int(input())


for i in range(1,c+1):
    sum=0
    avg=0
    data=list(map(int, input().split()))

    for j in range(1,data[0]+1):
        sum+=data[j]

    avg=sum/data[0]
    count=0

    for k in range(1,data[0]+1):
        if data[k]>avg:
            count+=1

    rate=count/data[0]*100
    print(f'{rate:.3f}%')