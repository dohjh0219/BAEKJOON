a,b=map(int,input().split())
div_a=[]
div_b=[]
common_div=[]

mul_a=[]
mul_b=[]

for i in range(1,a+1):
    if a%i==0:
        div_a.append(i)

for j in range(1,b+1):
    if b%j==0:
        div_b.append(j)
        if div_a.count(j)==1:
            common_div.append(j)

i=1

while True:
    mul_a.append(a*i)
    mul_b.append(b*i)
    if mul_b.count(a*i)==1:
        common_mul=a*i
        break
    elif mul_a.count(b*i)==1:
        common_mul=b*i
        break
    else:
        i+=1

print(max(common_div))
print(common_mul)