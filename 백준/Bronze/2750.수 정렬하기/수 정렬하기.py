n=int(input())
data=[]

for i in range(1,n+1):
    data.append(int(input()))
    
sor_data=list(sorted(data))

for i in range(1,len(sor_data)+1):
    print(sor_data[i-1])