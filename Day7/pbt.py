"""
그래프 그리기
터미널에서 pip install matplotlib 한뒤
pip list로 확인하기

불러오기 import
"import mat install matplotlib"
"""
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1, 2], [0, 1, 2], "r", [0, 1, 2], [0, 1, 4], "g")
plt.title("y=")
plt.show()
