n=int(input())

for i in range(1,n+1):
    score=0
    con='False'
    temp_score=0
    
    data=list(map(str,input()))

    if data[0]=="O":
        score=score+1
        temp_score=temp_score+1
        con='True'
    else:
        score=0
        con='False'

    for j in range(2,len(data)+1):
        if data[j-1]=="O":
            if con=='True':
                score=score+temp_score+1
            else :
                score=score+1
            temp_score=temp_score+1
            con='True'
        else:
            con='False'
            temp_score=0
    print(score)