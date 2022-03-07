m=int(input())
n=int(input())

result=[]
sumnum=0

for i in range(m,n+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if i!=1:
        if count==0:
            result.append(i)
            sumnum+=i

if len(result)==0:
    print('-1')
else:
    print(sumnum)
    print(result[0])