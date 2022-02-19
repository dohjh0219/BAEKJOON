a,b=map(int,input().split())

a_list=list(map(int,str(a)))
b_list=list(map(int,str(b)))

rev_a=100*a_list[2]+10*a_list[1]+a_list[0]
rev_b=100*b_list[2]+10*b_list[1]+b_list[0]

revlist=[rev_a,rev_b]

print(max(revlist))