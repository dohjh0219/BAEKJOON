import sys

n=int(sys.stdin.readline())

for i in range(n):
    bracket=0

    data=list(input())
    state='True'

    for k in range(len(data)):

        if data[k]=='(':
            if bracket>=0:
                bracket+=1
            else:
                if k!=0:
                    state='False'
                else:
                    bracket+=1
        else:
            if bracket>0:
                bracket-=1
            else:
                if k!=0:
                    bracket-=1
                else:
                    state='False'
        
        if k==len(data)-1:
            if state=='False':
                print('NO')
            elif bracket==0:
                print('YES')
            else:
                print('NO')