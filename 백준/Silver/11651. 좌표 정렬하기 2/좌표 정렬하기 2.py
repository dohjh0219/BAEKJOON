n=int(input())
array=[]


for i in range(n):
    array.append(list(map(int,input().split())))

array.sort(key=lambda x: (x[1],x[0]))  # 람다 표현식으로 array의 y-axis 먼저 sort. y-axis가 같다면 x-axis sort.

for j in range(n):
    print(array[j][0],array[j][1])