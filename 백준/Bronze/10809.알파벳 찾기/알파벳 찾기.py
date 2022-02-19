n = list(map(str, input()))
for i in range (97,123):
    for j in range(0, len(n)):
        a = -1
        if chr(i) == n[j]:
            a = j
            break
    print(a, end=' ')