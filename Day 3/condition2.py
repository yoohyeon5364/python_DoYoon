"""
조건문2
-while
while 조건:
    참일때 실행하는 코드
->무한으로 반복하고 싶다면
While True:
    print("hi")
-위를 보면 알 수 있듯이 true에 T를 대문자로 쓴다
-FOR의 경우
for 변수 in range(시작,끝,중간)
for로 작성 한것을 while로 바꿀 수 있고
while로 작성 한것을 for로 바꿀 수 있다
->while의 예
i = 0
while i < 3:
    print("hi")
    i += 1

"""

# while False:
#     print("민기 바보")

# i = 0
# while i < 3:
#     print("hi")
#     i += 1

# i = 0
# while i < 100:
#     print("오늘은 화요일")
#     i += 1

# i = 1
# while i < 11:
#     print(i)
#     i += 1

# i = 1
# while i < 11:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# i = 1
# while i < 11:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 1
# sum = 1
# while i < 100:
#     i += 1
#     sum += i
# print(sum)

# i = 1
# while i < 101:
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1

# i = 1
# sum = 1
# while i < 20:
#     i += 1
#     if i % 7 == 0:
#         sum *= i
# print(sum)

i = 1
sum1 = 0
sum2 = 1
while i < 100:
    i += 1
    if i % 2 == 0:
        sum1 += i
    if i % 2 == 1:
        sum2 += i
print(sum1 - sum2)
