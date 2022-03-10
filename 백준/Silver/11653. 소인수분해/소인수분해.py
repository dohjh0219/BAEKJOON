num = int(input())

list = []

i = 2
while num!=1:
    if num%i==0:
        num/=i  ## 왼쪽 값에서 오른쪽 값을 나눈 값을 왼쪽에 할당하는 연산자.
        list.append(i)
        i=2
    else:
        i+=1
        
for j in list:
    print(j)