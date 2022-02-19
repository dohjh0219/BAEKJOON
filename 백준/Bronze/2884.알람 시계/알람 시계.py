h,m=map(int,input().split())

if m-45<0:
    m=m+60-45;
    if h-1<0:
        h=h+24-1;
        print(h,m)
    else:
        h=h-1;
        print(h,m)
else:
    m=m-45;
    print(h,m)