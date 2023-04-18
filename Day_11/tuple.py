"""
튜폴(tuple)
-python에서 사용하는 자료 구조중 하나
-list와 비슷 
리스트는 대괄호를 이용,
But,튜플은 소괄호를 이용 함

'리스트와 튜플의 공통 점:indexing,slicing

'리스트와 튜플의 차이 점:
-리스트는 mutable값(변경 가능한 값)
-튜플은 immutable값(변경 불가능한 값)

"""

a = [1, 2, 3]
b = (1, 2, 3)

print(a, b)
print(type(a), type(b))
print(a[1])
print(b[1])
print(a[0])
print(b[2])
print(a[:2])
print(b[:2])
a[2] = 100
print(a)
a[2] = 10
print(a)
a[1] = 10
a[2] = 100
print(a)

b[2] = 100
print(b)
