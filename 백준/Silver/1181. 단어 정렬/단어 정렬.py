import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)  ## set으로 변환하여 중복값을 제거함.
lst = list(set_lst)  ## 중복제거 후 list로 변환.
lst.sort()  ## 괄호 안에 아무것도 없으므로 알파벳 순 정렬.(하위조건)
lst.sort(key = len)  ## 문자열 길이로 정렬.(상위조건)

for i in lst:
    print(i)

    ## 전체적인 순서는 하위조건 충족 후 상위조건 충족이다. 중요!