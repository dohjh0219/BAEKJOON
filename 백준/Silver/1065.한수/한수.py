numbers=list(range(1,1001))
sep_num=[]
hansu=[]

for i in range(1,1001):
    sep_num.append(list(map(int,str(numbers[i-1]))))
    
    if len(sep_num[i-1])==1:
        hansu.append(numbers[i-1])
    elif len(sep_num[i-1])==2:
        hansu.append(numbers[i-1])
    elif len(sep_num[i-1])==3:
        gongcha1=sep_num[i-1][0]-sep_num[i-1][1]
        gongcha2=sep_num[i-1][1]-sep_num[i-1][2]
        if gongcha1==gongcha2:
            hansu.append(numbers[i-1])

n=int(input())
count=0

for j in range(1,len(hansu)+1):
    if n>=hansu[j-1]:
        count+=1
    else:
        break
 
print(count)