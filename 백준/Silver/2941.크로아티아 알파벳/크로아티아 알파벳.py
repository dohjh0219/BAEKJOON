def number_killer2(i):
    data[i-1]=0
    data[i]=0

data=list(map(str,input()))

count=len(data)
for i in range(1,len(data)):
    if len(data)==1:
        break
    elif data[i-1]=='c':
        if data[i]=='=':
            count-=1
            number_killer2(i)
        elif data[i]=='-':
            count-=1
            number_killer2(i)
    elif data[i-1]=='d':
        if data[i]=='z':
            if len(data)==2:
                break
            elif data[i+1]=='=':
                count-=2
                data[i-1]=0
                data[i]=0
                data[i+1]=0
        elif data[i]=='-':
            count-=1
            number_killer2(i)
    elif data[i-1]=='l':
        if data[i]=='j':
            count-=1
            number_killer2(i)
    elif data[i-1]=='n':
        if data[i]=='j':
            count-=1
            number_killer2(i)
    elif data[i-1]=='s':
        if data[i]=='=':
            count-=1
            number_killer2(i)
    elif data[i-1]=='z':
        if data[i]=='=':
            count-=1
            number_killer2(i)
    else:
        data[i-1]=0

print(count)