word=list(str(input()))

asc_word=[]    # 각 알파벳 별 아스키코드 기입
count_word=[]   # 알파벳 순서, 알파벳 반복 수 기입

for s in range(65,91):
    count_word.append(0)

for i in range(1,len(word)+1):
    asc_word.append(ord(word[i-1]))

for j in range(1,len(word)+1):
    for k in range(65,91):   # 알파벳 순서
        if asc_word[j-1]==k:
            count_word[k-65]+=1
        elif asc_word[j-1]==k+32:
            count_word[k-65]+=1

storage=[]
for y in range(65,91):
    if count_word[y-65]==max(count_word):
        storage.append(y)


if len(storage)==1:
    print(chr(storage[0]))
else:
    print('?')