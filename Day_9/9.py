import matplotlib.pyplot as plt

plt.figure()
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

for i in range(-10, 11):
    x1.append(i)
    y1.append(i)
    x2.append(i)
    y2.append(i**3)
    x3.append(i)
    y3.append(-(i**3))
plt.plot(x1, y1, x2, y2, x3, y3)
plt.show()

# b = []
# for i in range(2, 5):
#     b.append(i)

# print(b)

# figure, axes = plt.subplots(2, 2)
# x1 = []
# y1 = []
# for i in range(-10, 11):
#     x1.append(i)
#     y1.append(i**2)
# fruits = ["apple", "banana", "blueberry", "orange"]
# counts = [4, 6, 5, 10]
# bar_color = ["red", "yellow", "blue", "orange"]
# bar_color1 = ["black"]
# bar_color2 = ["red"]
# axes[0, 0].plot(x1, y1, "og")
# axes[0, 1].barh(fruits, counts, color=bar_color2)
# axes[1, 0].barh(fruits, counts, color=bar_color1)
# axes[1, 1].bar(fruits, counts, color=bar_color)
# plt.show()
