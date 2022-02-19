i=0;
j=0;

num=int(input())
new=int(num)

while j==0:
    list_num=list(map(int,str(new)))
    if len(list_num)==1:
        add=list_num[0]
    else:
        add=list_num[0]+list_num[-1]
    list_add=list(map(int,str(add)))
    add=list_add[-1]

    new=add+list_num[-1]*10
    i=i+1

    if num==new:
        print(i)
        j=1
    else:
        j=0