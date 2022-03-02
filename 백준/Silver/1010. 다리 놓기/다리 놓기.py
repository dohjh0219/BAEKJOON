def factorial(num):
    ans=1
    for j in range(1,num+1):
        ans=ans*j

    return ans

n=int(input())

for i in range(0,n):
    a, b=map(int,input().split())

    print(int(factorial(b)/(factorial(a)*factorial(b-a))))