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

리스트와 리스트를 합칠때'+' 사용합니다. (4칙연산중 +만 사용 가능)
ㅡ> 메소드는 extend

리스트를 비울때 'clear' 메소드를 사용합니다.

특정 위치에 값을 추가할때 'insert' 메소드를 사용합니다.

값이 몇번째 있는지 찾을때 'index' 메소드를 사용합니다.

값이 몇개가 있는지 알아볼때 'count' 메소드를 사용합니다.

리스트의 길이를 알고싶을때 'len' 함수를 사용합니다.


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

# a = [1, 2]
# b = [3, 4]
# a.extend(b)
# print(a)

# d = [100, 200]
# d.clear()
# print(d)

# e = [1, 2, 3]
# e.insert(1, 100)
# print(e)

# f = [1, 2, 3, 4]
# print(f.index(3))

# f = [1, 2, 3, 4, 2]
# print(f.index(2))

# f = [1, 2, 3, 4, 2]
# print(f.count(2))

# h = [1, 2, 3, 4]
# print(len(h))

# h.pop()
# h.remove(1)
# print(len(h))

# a = ["반나ㅏ냐", "사ㅏ고ㅓㅏ", "오ㄹ ㅔㄴ지"]

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

# Q1.
# fruit = ["orange", "cherry", "watermwlon", "bluberry", "apple"]
# fruit.sort()
# fruit.reverse()
# for i in fruit:
#     print(i)

# phonenumber = [0, 1, 0, 1, 2, 3, 4, 5, 6, 7]
# phonenumber.clear()
# phonenumber.append(0)
# phonenumber.append(1)
# phonenumber.append(0)
# phonenumber.append(9)
# phonenumber.append(8)
# phonenumber.append(7)
# phonenumber.append(6)
# phonenumber.append(5)
# phonenumber.append(4)
# phonenumber.append(3)
# print(phonenumber)

# 함수랄까 = []
# for i in range(1, 21):
#     if i % 3 == 0:
#         함수랄까.append(i)
#         함수랄까.sort()
#     함수랄까.reverse()
# print(함수랄까)

# def GCD ():
#         for i in range(x,y):

# a = [10, 20, 30]
# a.insert(1, 100)
# a.insert(3, 200)
# print(a)

# fruit = ["orange", "banana", "cherry", "apple"]
# print(fruit[0])
# print(fruit[1])
# print(fruit[2])
# print(fruit[3])

# fruit1 = ["orange", "banana", "cherry", "apple"]
# fruit1.sort()
# print(fruit1[0])
# print(fruit1[1])
# print(fruit1[2])
# print(fruit1[3])

# fruit2 = ["orange", "banana", "cherry", "apple"]
# fruit2.sort()
# fruit2.reverse()
# print(fruit2[0])
# print(fruit2[1])
# print(fruit2[2])
# print(fruit2[3])

# fruit = ["orange", "banana", "cherry", "apple"]
# fruit.append("watermelon")
# fruit.append("blueberry")
# fruit.append("tomato")
# fruit.sort()
# fruit.reverse()
# for i in range(len(fruit)):
#     print(fruit[i])

# fruits = ["orange", "banana", "cherry", "apple"]
# for fruit in fruits:
#     print(fruit)

# a = []
# for i in range(1, 6):
#     a.append(i)
# print(a)
# for i in range(len(a)):
#     print(a[i])

b = []
for i in range(1, 21):
    if i % 3 == 0:
        b.append(i)
print(b)
b.sort
b.reverse
for i in range(len(b)):

    print(b[i])

c = []
for i in range(1, 101):
    if i % 3 == 0:
        if i % 4 == 0:
            c.append(i)
c.sort()
c.reverse()
print(c)

c.sort()
for i in range(len(c)):
    print(c[i])
