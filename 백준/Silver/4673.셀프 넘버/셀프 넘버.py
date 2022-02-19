number=list(range(1,10001))  #1부터 10000까지의 숫자 리스트 생성

delete_list=[]

for i in number :  # 숫자 리스트에서 받아 i에 대입하는 반복문
    for j in str(i):  # str(i)를 통해 분석 중인 숫자를 문자열로 변환
        i+=int(j)    # 분석중인 숫자=분석중인 숫자+str(i)-->각 자리 수
    if i <= 10000:  # 해당 숫자가 10000넘으면 안됨.
        delete_list.append(i)   # 분석중인 숫자를 딜리트리스트에 추가.(이 숫자는 셀프넘버가 아님.)

for delete_num in set(delete_list):  # 리스트형을 set자료형으로 변환(why? 중복값 제거를 위해)
    number.remove(delete_num)   # 숫자리스트에서 셀프넘버가 아닌 숫자 삭제
for self_num in number :
    print(self_num)