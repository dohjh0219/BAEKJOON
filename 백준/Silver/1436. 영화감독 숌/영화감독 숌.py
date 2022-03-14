n=int(input())

initial=666

while n!=0:
    if '666' in str(initial):
        n-=1  # 분석하고 있는 initial에 666이 있으면 n을 감소.
    initial+=1  # 무작정 initial에 1 더하기.
    
print(initial-1)  # n이 0이 되었을 때 불필요하게 initial을 1 증가시켰으므로 이를 해소하여 출력.