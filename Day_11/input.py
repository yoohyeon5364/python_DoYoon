"""
input(입력 함수)
-python 내부로 사용자의 값을 전달 할떄 사용함
-엔터가 입력 될 때 까지 기다림
-입력 받은 값은 항상 문자로 인식 함
-숫자로 변경하기 위해서는 int가 필요
"""

num1 = input("첫 번째 수:")
num2 = input("두 번쨰 수:")
str = f"첫번째 수는 {num1},두번째 수는{num2},두수의 합은{int(num1)+int(num2)}"
print(str)
