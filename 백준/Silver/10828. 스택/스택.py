import sys

n=int(sys.stdin.readline())

stack=[]

for i in range(n):
    data=sys.stdin.readline().split()  # split으로 한번 입력된 것을 나누어 저장하기
    prompt=data[0]  # 앞서 입력 받은 내용의 앞 부분을 저장

    if prompt=='push':
        stack.append(data[1])

    elif prompt=='pop':
        if len(stack)==0:
            print('-1')
        else: 
            print(stack.pop())

    elif prompt=='size':
        print(len(stack))

    elif prompt=='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')

    elif prompt=='top':
        if len(stack)==0:
            print('-1')
        else:
            print(stack[len(stack)-1])