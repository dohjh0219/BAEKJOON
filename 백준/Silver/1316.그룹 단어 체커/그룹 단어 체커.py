def find_index(data,target):
    res=[]
    lis=data

    for s in range(1,len(lis)+1):
        if lis[s-1]==target:
            res.append(s-1)
    return res

n=int(input())
result=0

for i in range(1,n+1):
    word=list(map(str,input()))
    asc_word=[]
    adress=[]
    con_result=0
    
    for j in range(1,len(word)+1):
        asc_word.append(ord(word[j-1]))

    for k in range(97,123):
        if asc_word.count(k)>1:
            adress.append(find_index(asc_word,k))
        
    if len(adress)==0:
        result+=1
    else:
       for u in range(1,len(adress)+1):
            for d in range(1, len(adress[u-1])):
                if adress[u-1][d]-adress[u-1][d-1]!=1:
                     con_result-=1
                     break
            con_result+=1
       if con_result==len(adress):
            result+=1

print(result)