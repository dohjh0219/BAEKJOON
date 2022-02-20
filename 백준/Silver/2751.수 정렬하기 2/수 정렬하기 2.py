n=int(input())
data=[]

for i in range(1,n+1):
    data.append(int(input()))

data.sort()

for j in data:
    print(j)