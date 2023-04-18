"""
f-string(f문자열)
-문자열 과 변수를 혼합하여 시용할 때 작성

-문법:f"문자열{변수}"
-변수를 쓸때는 중괄호를 묶어서 사용
-변수 자리에 연산자와 함수도 사용 가능 함
"""

day = "수"
str = f"오늘은 {day}요일 입니다"
print(str)

age = 40
name = "윤성"
str = f"저는 {age}살이고, 이름은 {name}이에요"
print(str)

season = "겨울"
month = 12
day = 25
str = f"오늘 계절은 {season}이고, {month}이고 {day}일 입니다"
print(str)

num1 = 10
num2 = 20
str = f"첫번째 숫자는 {num1}이고, 두번째 숫자는 {num2}이면 두수의 합은 {num1+num2}입니다"
print(str)

num1 = 100
num2 = 200
str = f"첫번째 숫자는 {num1}이고, 두번째 숫자는 {num2}이면 두수의 합은 {num1+num2}입니다"
print(str)
