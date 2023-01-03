# """
# if 조건 :
# -> 참일떄
# else :
# -> 거짓일때
# """
# """
# if 조건1 :
# -> 참일떄
# elif 조건2 :
# -> 조건 1은 거짓, 조건2 참
# else :
# -> 모두 거짓
# """
# # if 예제
# apple = 10
# orange = 20
# if apple > orange:
#     print("apple bigger than orange")
# else:
#     print("orange bigger than apple")

# # 1
# Math = 100
# English = 100

# if Math > English:
#     print("Math is better than English")
# elif Math < English:
#     print("English is better than Math")
# else:
#     print("English anf Math are Similar")

# """
# for 예제
# 자바스크립트라면>
# for (var i = 0 ; i < 3 ; i++){
#     console.log("안녕");
# }

# 파이썬>
# for i in range(3):
#     print("안녕")
# """

# # 1 (1~10 print)
# for i in range(10):
#     print(i + 1)

# """
# range() 괄호 안에 넣은 수 많큼 반복, ex) print () 괄호 언애 i - 1을 한다면 1씩 줄어들면서 프린트 될 것
# 다른 방법> fo i in range(1,11):

# for 3가지
# 숫자 1 > for i in range(10):
# 범위(숫자 2) > for i ni range(0,10):
# 범위, 증감 (숫자 3) > for i in range(0,10,1):
#                print(i)
# """
# # 2
# for i in range(1, 11):
#     if i % 2 == 1:
#         print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# # 3
# sum = 0
# for i in range(10, 21):
#     if i % 3 == 0:
#         sum += i
# print(sum)

# # 4
# sum1 = 0
# sum2 = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum1 += i
#     elif i % 2 == 1:
#         sum2 += i
# print(sum1 - sum2)

# # 5
# for i in range(50, 81):
#     if i % 3 == 0:
#         if i % 4 == 0:
#             print(i)

# # 6
# sum = 1
# for i in range(1, 21):
#     if i % 5 == 0:
#         sum *= i
# print(sum)

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

for i in range(1, 101):
    if i % 3 == 0 and i % 4 == 0 and i % 5 == 0:
        print(i)
