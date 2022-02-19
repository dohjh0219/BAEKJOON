number=list(map(int,input().split()))

maxnum=max(number)
number.remove(maxnum)
print(max(number))