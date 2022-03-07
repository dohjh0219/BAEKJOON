import sys

n=int(input())

check=[0]*10001  # 숫자의 카운트 넣는 곳

for i in range(n):
    input_num=int(sys.stdin.readline())  ## 시간초과 방지하기 위해 sys이용
    check[input_num]+=1

for i in range(10001):
    if check[i]!=0:  ## 카운트가 한번이라도 되었다면
        for j in range(check[i]):
            print(i)  ## 카운트 만큼 i값 출력