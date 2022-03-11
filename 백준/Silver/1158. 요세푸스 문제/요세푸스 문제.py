N,K = map(int,input().split())
data=[i for i in range(1,N+1)]    # 기본 자연수 리스트

answer = []   # 제거 자연수 리스트
num = 0  # 제거될 인덱스 번호

for t in range(N):
    num += K-1  
    if num >= len(data):   # 전체 N보다 많은 경우(원을 한바퀴 다 돌아버린 경우)
        num = num%len(data)
 
    answer.append(str(data.pop(num)))

print("<",", ".join(answer)[:],">", sep='')