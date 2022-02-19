a1=int(input())
a2=int(input())

list_a1=list(map(int, str(a1)))
list_a2=list(map(int, str(a2)))

print(a1*int(list_a2[2]))
print(a1*int(list_a2[1]))
print(a1*int(list_a2[0]))
print(a1*a2)