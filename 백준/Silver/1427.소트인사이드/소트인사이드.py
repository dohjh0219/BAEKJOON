num=list(map(int,input()))


for i in range(1,len(num)+1):
    num.sort(reverse=True)

print("".join(map(str,num)))