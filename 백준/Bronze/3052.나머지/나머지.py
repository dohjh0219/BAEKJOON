data=[input() for i in range(10)]
per=[]

for i in range(1,11):
    per.append(int(data[i-1])%42)

sum=0

for j in range(1,43):
    if per.count(j-1)>0:
        sum+=1

print(sum)