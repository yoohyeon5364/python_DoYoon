"""
리스트
열거형 변수를 나타내는 자료 구조 중 하나

열거-> 기차를 떠올리자
ㄴ> 여러 면수를 모음
    ㄴ> visiual studio code : ex) [a,b,c]

오른쪽 부터 -1 왼쪽 부터 0

indexing : list 안에 있는 것을 순서대로 빼 올 수 있다
            0 1 2
            a,b,c 

빈 리스트만드는 법
ex) a=[] 
    ㄴ> 자료가 안에 없지만 리스트의 형태를 가춘 것

추가하는 메소드 (맨 뒤에 추가)
<특징1> ex) d.append[1]
        ex) d.append[2]

제거하는 메소드 (맨 뒤에 추가)
<특징2> ex) d.pop[1]
        ex) d.pop[2]

선택해서 제거하는 메소드 
<특징3> ex) d=[1,2,3,4]
        ex) d.remove(3)

정력(오름차순) 메소드 
<특징4> ex) e=[1,3,2,4]
        ex) e.sort(3)

반대로 정렬하는 메소드
<특징5> ex) g.reverse[1,2,3,4]
        ex) g.reverse()

내림차순(응용)        
<응용1> sort()
       reverse()
"""

# d = []
# d.append(1)
# d.append(2)

# print(d)

# # *원래 숙제 였던것]
# 결과 = []
# for i in range(1, 21):
#     if i % 3 == 0:
#         결과.append(i)

# 결과.reverse()
# print(결과)

# # Q1. 1~10 중 4의 배수가 아닌 수들을 내림차 순 리스트로 출력
# 결과1 = []
# for i in range(1, 11):
#     if i % 4 != 0:
#         결과1.append(i)

# 결과1.reverse()
# print(결과1)
# # Q2. 구구단(3) [27,24,.....9,6,3] or 구구단(7) [63,56,.....21,14,7]
# 결과2 = []


# def gogodan(num):
#     for i in range(1, 10):
#         결과2.append(num * i)
#         결과2.reverse()
#     print(결과2)


# gogodan(3)
# gogodan(7)

# Q3.짝수(3) ex) 6,4,2
# def jjaksoo(num):
#     결과3 = []
#     for i in range(1, num * 2 + 1):
#         if i % 2 == 0:
#             결과3.append(i)
#     결과3.reverse()
#     print(결과3)


# jjaksoo(3)
# jjaksoo(6)
# jjaksoo(4)

# a = [2, 4, 3, 1]
# a.sort()
# a.reverse()
# print(a)
