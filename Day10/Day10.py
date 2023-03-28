"""
.slicing
전체 중  일부만 선택하는 방법
"""
import numpy as np

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = np.array([1, 2, 3, 4, 5])
d = np.array([6, 7, 8, 9, 10])
print(c / d)

fruits = ["apple", "banana", "orange", "watermelon"]
print(fruits[2:])
"""
문법 
리스트[시작+끝]
      이상  미만
#":"="~"
"""

J = []
for i in range(20, 30, 2):
    if i % 3 != 0:
        J.append(i)
print(J[:4])
